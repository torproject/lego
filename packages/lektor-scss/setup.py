#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
import io
import re

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

setup(
    author='L3D',
    author_email='l3d@c3woc.de',
    description='Lektor plugin to compile css out of sass - based on libsass',
    keywords='Lektor plugin',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-scss',
    packages=find_packages(),
    py_modules=['lektor_scss'],
    url='https://github.com/chaos-bodensee/lektor-scss.git',
    version='1.4.1',
    install_requires  =  [
        "libsass==0.21.0", "termcolor",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Framework :: Lektor',
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'lektor.plugins': [
            'scss = lektor_scss:scssPlugin',
        ]
    }
)
