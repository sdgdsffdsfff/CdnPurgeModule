#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.0.1'
requires = ['requests','gevent']


setup(
    name='cdnpurge',
    version=version,
    description='varnish purge',
    url='https://github.com/rfyiamcool',
    packages=['cdnpurge'],
    install_requires=requires,
    ),
)
