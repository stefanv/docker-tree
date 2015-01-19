from __future__ import print_function
import networkx as nx
from asciitree import draw_tree


def graph_from_images(docker_images):
    """Convert Docker image listing to a NetworkX graph.

    Parameters
    ----------
    docker_images : dict
        Output given by ``docker_client.images()``.

    Returns
    -------
    dg : networkx.DiGraph
        Directed dependency graph of images.

    """
    dg = nx.DiGraph()

    for image in docker_images:
        dg.add_node(image['Id'], tags=image['RepoTags'])
        dg.add_node(image['ParentId'], tags=image['RepoTags'])
        dg.add_edge(image['ParentId'], image['Id'])

    return dg


def root(dg):
    """Return the root of the directed graph.

    Parameters
    ----------
    dg : networkx.DiGraph
        Graph of images.

    Returns
    -------
    root : str
        Name of root image.
    """
    return [n for n in nx.topological_sort(dg) if n != ''][0]


def draw_ascii_tree(directed_graph):
    def child_iter(node):
        "Return an iterator over the children of `node`"
        return directed_graph.successors(node)
    def text_str(node):
        "Return a text representation of `node`."
        return node[:12]

    return draw_tree(root(directed_graph), child_iter, text_str)
