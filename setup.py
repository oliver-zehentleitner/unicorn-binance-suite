#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘UNICORN Binance Suite’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-suite
# Github: https://github.com/oliver-zehentleitner/unicorn-binance-suite
# Documentation: https://oliver-zehentleitner.github.io/unicorn-binance-suite
# PyPI: https://pypi.org/project/unicorn-binance-suite
#
# License: MIT
# https://github.com/oliver-zehentleitner/unicorn-binance-suite/blob/master/LICENSE
#
# Author: Oliver Zehentleitner
#
# Copyright (c) 2019-2025, Oliver Zehentleitner (https://about.me/oliver-zehentleitner)
#
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='unicorn_binance_suite',
     version='2.0.0',
     author="Oliver Zehentleitner",
     url="https://github.com/oliver-zehentleitner/unicorn-binance-suite",
     description="The UNICORN Binance Suite is a comprehensive collection of open-source Python packages designed "
                 "for building sophisticated automated trading systems. Tailored for Python developers, this suite "
                 "offers seamless integration with the Binance API, enabling the creation of advanced and professional "
                 "trading bots for streamlined and efficient cryptocurrency trading.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT',
     install_requires=['unicorn-binance-websocket-api>=2.0.0', 'unicorn-binance-rest-api>=2.0.0', 'unicorn-fy>=0.13.1',
                       'unicorn-binance-local-depth-cache>=1.0.0', 'unicorn-binance-trailing-stop-loss>=1.0.0'],
     keywords='Binance, Websocket, REST, Local Depth Cache, Trailing Stop Loss, Trading Bot, Algo Trading',
     project_urls={
        'Documentation': 'https://oliver-zehentleitner.github.io/unicorn-binance-suite/',
        'Changes': 'https://oliver-zehentleitner.github.io/unicorn-binance-suite/changelog.html',
        'License': 'https://oliver-zehentleitner.github.io/unicorn-binance-suite/license.html',
        'Issue Tracker': 'https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues',
        'Wiki': 'https://github.com/oliver-zehentleitner/unicorn-binance-suite/wiki',
        'Author': 'https://www.linkedin.com/in/oliver-zehentleitner',
        'Telegram': 'https://t.me/unicorndevs',
     },
     python_requires='>=3.8.0',
     packages=find_packages(exclude=["tools", "images", "dev", "docs", ".github"]),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
         "Programming Language :: Python :: 3.11",
         "Programming Language :: Python :: 3.12",
         "Programming Language :: Python :: 3.13",
         'Intended Audience :: Developers',
         "Intended Audience :: Financial and Insurance Industry",
         "Intended Audience :: Information Technology",
         "Intended Audience :: Science/Research",
         "Operating System :: OS Independent",
         "Topic :: Office/Business :: Financial :: Investment",
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
)

