#!/usr/bin/env python

# See
# http://docker-py.readthedocs.org/en/latest/api/
# for commands supported by the docker-py API
from __future__ import print_function
from docker import Client
from docker.utils import kwargs_from_env
from requests.exceptions import ConnectionError
from .tree import draw_ascii_tree, graph_from_images
import argparse
from .argparse_commands import parse_commands

import sys


def docker_client(client_args={}):
    try:
        args = kwargs_from_env(assert_hostname=False)
        args.update(client_args)
        cli = Client(**args)
        cli.version()
    except ConnectionError:
        return None

    return cli


def main():
    parser = argparse.ArgumentParser(description='Docker Tree')
    cmd_parsers = parser.add_subparsers(help=' - sub-commands -',
                                        dest='subparser_name')

    tree_parser = cmd_parsers.add_parser('tree', help='Print a tree of images')
    prune_parser = cmd_parsers.add_parser('prune', help='Remove dangling images')

    parser.add_argument('extra', nargs="*", help=argparse.SUPPRESS)

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()
    cmd_args = parse_commands(parser, args)
    cmd = args.subparser_name

    cli = docker_client(client_args={'version': '1.15'})

    if cli is None:
        print("Error: could not establish connection to the Docker server")
        sys.exit(-1)

    if cmd == 'tree':
        dg = graph_from_images(cli.images(all=True))
        print(draw_ascii_tree(dg))
    elif cmd == 'prune':
        print('Pruning')
