from setuptools import setup

setup(
    name='docker-tree',
    version='0.1',
    description='Visualize and clean up Docker images',
    url='https://github.com/stefanv/docker-tree',
    license='Modified BSD',
    packages=['docker_tree'],
    entry_points = {
        'console_scripts': ['docker-tree = docker_tree.command_line:main']
    }
)
