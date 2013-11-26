#!/usr/bin/env python

import os
import sys

from distutils.core import setup


def publish():
        """Publish to PyPi"""
        os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
        publish()
        sys.exit()

required = []

setup(
        name='underdict',
        version='0.0.1',
        description='A data structure similar to a dictionary with a collection of functional utilities.',
        long_description=open('README.md').read()),
        author='Rodrigo Guzman',
        author_email='rodguze@gmail.com',
        url='https://github.com/rz/underdict',
        packages= [
                'underdict',
        ],
        install_requires=required,
        license='LICENSE.txt',
        classifiers=(
                'Intended Audience :: Developers',
                'Natural Language :: English',
                'License :: OSI Approved :: MIT License',
                'Programming Language :: Python',
        ),
)