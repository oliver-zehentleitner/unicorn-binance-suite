#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/sphinx/install_sphinx.sh
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

python3 -m pip install sphinx --upgrade
python3 -m pip install python-docs-theme-lucit --upgrade
python3 -m pip install rich --upgrade
python3 -m pip install myst-parser --upgrade
python3 -m pip install sphinx-markdown-tables --upgrade