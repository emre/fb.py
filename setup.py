#!/usr/bin/env python

from setuptools import setup

setup(name='fbpy',
    version='1.0',
    description='python sdk for facebook apis',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    url='http://github.com/egnity/fb.py',
    package_dir={'': 'src'},
    packages = ["fbpy", "fbpy/tools",]
)

