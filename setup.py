#!/usr/bin/env python3
# coding=utf-8

"""
python distribute file
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)

from setuptools import setup, find_packages


def requirements_file_to_list(fn="requirements.txt"):
    """read a requirements file and create a list that can be used in setup.

    """
    with open(fn, 'r') as f:
        return [x.rstrip() for x in list(f) if x and not x.startswith('#')]


setup(
    name="checkportmon",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements_file_to_list(),
    dependency_links=[
        # If your project has dependencies on some internal packages that is
        # not on PyPI, you may list package index url here. Then you can just
        # mention package name and version in requirements.txt file.
    ],
    entry_points={
        'console_scripts': [
            'main = checkportmon.main:main',
        ]
    },
    package_data={
        'checkportmon': ['logger.conf']
    },
    author="Shibhikkiran Devadoss",
    author_email="shibhi@example.com",
    maintainer="Shibhikkiran Devadoss",
    maintainer_email="shibhi@example.com",
    description="Check network port connectivity",
    long_description=open('README.md').read(),
    license="GPLv2+",
    url="https://pypi.python.org/pypi/checkportmon",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)
