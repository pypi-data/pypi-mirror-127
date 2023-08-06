#!/usr/bin/env python

from setuptools import setup

setup(
    name='blather',
    version='0.0.1',
    packages=['blather'],
    install_requires=[
        'torch',
        'transformers',
    ],
)