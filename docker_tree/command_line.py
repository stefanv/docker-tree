#!/usr/bin/env python

# See
# http://docker-py.readthedocs.org/en/latest/api/
# for commands supported by the docker-py API
from docker import Client
from requests.exceptions import ConnectionError

import argparse
from .argparse_commands import parse_commands

import sys


def docker_client(server_urls, client_args={}):
    try:
        cli = Client(**kwargs_from_env(assert_hostname=False))
        cli.version()
        return cli
    except ConnectionError:
        pass

    for url in server_urls:
        cli = Client(base_url=url, **client_args)

        try:
            cli.version()
        except ConnectionError:
            pass
        else:
            return cli

    return None


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

    cli = docker_client(server_urls=['unix://var/run/docker.sock',
                                     'tcp://127.0.0.1:2375'],
                        client_args={'version': '1.0'})

    if cli is None:
        print("Error: could not establish connection to the Docker server")
        sys.exit(-1)

    if cmd == 'tree':
        print(cli.images(all=True))
    elif cmd == 'prune':
        print('Pruning')
