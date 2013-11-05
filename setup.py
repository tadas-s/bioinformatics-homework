try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Tadas',
    'name': 'skeleton',
    'install_requires': ['nose', 'mock']
}

setup(requires=['nose', 'mock']**config, requires=['mock', 'nose'])
