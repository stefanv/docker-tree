from docker_tree.tree import graph_from_images, root

import json
import os

data_path = os.path.dirname(__file__)

with open(os.path.join(data_path, 'response.json')) as f:
    image_data = json.load(f)


def test_image_data_parse():
    dg = graph_from_images(image_data)
    assert root(dg).startswith('5111')
