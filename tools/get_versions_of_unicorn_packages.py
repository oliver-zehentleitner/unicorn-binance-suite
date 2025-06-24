#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: tools/get_versions_of_unicorn_packages.py
#
# Part of ‘UNICORN Binance Suite’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-suite
# Github: https://github.com/oliver-zehentleitner/unicorn-binance-suite
# Documentation: https://oliver-zehentleitner.github.io/unicorn-binance-suite
# PyPI: https://pypi.org/project/unicorn-binance-suite
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2022-2023, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
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

import logging

logging.basicConfig(level=logging.ERROR,
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

try:
    import unicorn_fy
    unify_version = unicorn_fy.UnicornFy().get_version()
except ModuleNotFoundError:
    unify_version = "not found"

try:
    import unicorn_binance_local_depth_cache
    ubldc = unicorn_binance_local_depth_cache.BinanceLocalDepthCacheManager(warn_on_update=False)
    ubldc_version = ubldc.get_version()
    ubldc.stop_manager()
except ModuleNotFoundError:
    ubldc_version = "not found"

try:
    from unicorn_binance_rest_api.manager import BinanceRestApiManager
    with BinanceRestApiManager(warn_on_update=False) as ubra:
        ubra_version = ubra.get_version()
except ModuleNotFoundError:
    ubra_version = "not found"

try:
    import unicorn_binance_trailing_stop_loss
    ubtsl = unicorn_binance_trailing_stop_loss.BinanceTrailingStopLossManager(warn_on_update=False, start_engine=False)
    ubtsl_version = ubtsl.get_version()
    ubtsl.stop_manager()
except ModuleNotFoundError:
    ubtsl_version = "not found"

try:
    import unicorn_binance_websocket_api
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(warn_on_update=False)
    ubwa_version = ubwa.get_version()
    ubwa.stop_manager()
except ModuleNotFoundError:
    ubwa_version = "not found"

try:
    from lucit_licensing_python.manager import LucitLicensingManager
    with LucitLicensingManager(start=False) as llm:
        llm_version = llm.get_module_version()
except ModuleNotFoundError:
    llm_version = "not found"

print(f"Please post this to your github issue:")
print(f"lucit_licensing_python: {llm_version}")
print(f"unicorn_fy: {unify_version}")
print(f"unicorn_binance_local_depth_cache: {ubldc_version}")
print(f"unicorn_binance_rest_api: {ubra_version}")
print(f"unicorn_binance_trailing_stop_loss: {ubtsl_version}")
print(f"unicorn_binance_websocket_api: {ubwa_version}")
