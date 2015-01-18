#!/usr/bin/env python

# See
# http://docker-py.readthedocs.org/en/latest/api/
# for commands supported by the docker-py API
from docker import Client
from requests.exceptions import ConnectionError

import sys


def docker_client(server_urls, client_args={}):
    for url in server_urls:
        cli = Client(base_url=url, **client_args)

        try:
            cli.version()
        except ConnectionError:
            pass
        else:
            return cli

    return None


cli = docker_client(server_urls=['unix://var/run/docker.sock',
                                 'tcp://127.0.0.1:2375'],
                    client_args={'version': '1.0'})

if cli is None:
    print("Error: could not establish connection to the Docker server")
    sys.exit(-1)

print(cli.images())
