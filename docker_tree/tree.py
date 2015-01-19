import networkx as nx


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
    return dg.successors('')[0]
