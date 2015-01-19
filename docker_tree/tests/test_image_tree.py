from docker_tree.tree import graph_from_images, root, draw_ascii_tree

import json
import os

data_path = os.path.dirname(__file__)

with open(os.path.join(data_path, 'response.json')) as f:
    image_data = json.load(f)


def test_image_data_parse():
    dg = graph_from_images(image_data)
    assert root(dg).startswith('5111')


def test_draw_tree():
    dg = graph_from_images(image_data)
    assert draw_ascii_tree(dg).startswith('5111')


def test_draw_tree_2():
    dg = graph_from_images(image_data)
    assert '\n  +--' in draw_ascii_tree(dg)
