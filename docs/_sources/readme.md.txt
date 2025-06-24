[![GitHub Release](https://img.shields.io/github/release/LUCIT-Systems-and-Development/unicorn-binance-suite.svg?label=github)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/LUCIT-Systems-and-Development/unicorn-binance-suite/total?color=blue)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/releases)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-binance-suite?color=blue)](https://pypi.org/project/unicorn-binance-suite/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-binance-suite)](https://pepy.tech/project/unicorn-binance-suite)
[![License](https://img.shields.io/badge/license-LSOSL-blue)](https://oliver-zehentleitner.github.io/unicorn-binance-suite/license.html)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_binance_suite.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_binance_suite.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues)
[![codecov](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-binance-suite/branch/master/graph/badge.svg?token=5I03AZ3F5S)](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-binance-suite)
[![CodeQL](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/codeql-analysis.yml)
[![Unit Tests](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/unit-tests.yml)
[![Build and Publish GH+PyPi](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/build_wheels.yml)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://oliver-zehentleitner.github.io/unicorn-binance-suite/)
[![Read How To`s](https://img.shields.io/badge/read-%20howto-yellow)](https://technopathy.club)
[![GitHub](https://img.shields.io/badge/source-github-cbc2c8)](https://github.com/oliver-zehentleitner/unicorn-binance-suite)
[![Telegram](https://img.shields.io/badge/community-telegram-41ab8c)](https://t.me/unicorndevs)

[![LUCIT-UBS-Banner](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/logo/LUCIT-UBS-Banner-Readme.png)](https://github.com/oliver-zehentleitner/unicorn-binance-suite)

# UNICORN Binance Suite
[Description](#description) | [Installation](#installation-and-upgrade) | [How To](#howto) | [Change Log](#change-log) | 
[Documentation](#documentation) | [Social](#social) | [Bugs](#how-to-report-bugs-or-suggest-improvements) | 
[Contributing](#contributing) | [Disclaimer](#disclaimer)

## Description
The [`UNICORN Binance Suite`](https://github.com/oliver-zehentleitner/unicorn-binance-suite) is a comprehensive collection of open-source Python packages designed for 
building sophisticated automated trading systems. Tailored for Python developers, this suite offers seamless 
integration with the Binance API, enabling the creation of advanced and professional trading bots for streamlined and 
efficient cryptocurrency trading.

The suite is the most stable, powerful and convenient way to interact with various Binance API endpoints via 
[REST](https://www.lucit.tech/unicorn-binance-rest-api.html) and 
[Websocket](https://www.lucit.tech/unicorn-binance-websocket-api.html) and to 
[manage local order books](https://www.lucit.tech/unicorn-binance-local-depth-cache.html) and 
[trailing stop losses](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html).

All libraries in the suite are coordinated with each other, interlock perfectly, are fully documented and offer 
standardized interfaces and tools for the programmer. LUCIT continuously develops the modules, fixes bugs, tests the 
libraries extensively and offers [fast, direct and free support](https://www.lucit.tech/get-support.html).

All modules are delivered optimized as PyPy and as Python C Extension (Cython) via 
[PyPi](https://pypi.org/user/LUCIT/) and [Anaconda](https://anaconda.org/lucit). The package 
creation runs completely transparently directly from the respective GitHub repository through GitHub Actions and is 
deployed directly to PyPi and Anaconda in a traceable manner. This process makes it tamper-proof for you to 
understand which code is contained in which package and can therefore easily install optimized builds for the platform, 
architecture and Python version used.

## Modules of the UNICORN Binance Suite

- [`UNICORN Binance Local Depth Cache`](https://www.lucit.tech/unicorn-binance-local-depth-cache.html): A Python SDK from LUCIT to access and manage multiple local Binance 
  DepthCaches with Python in a simple, fast, flexible, robust and fully-featured way. 
- [`UNICORN Binance REST API`](https://www.lucit.tech/unicorn-binance-rest-api.html): A Python SDK by LUCIT to use the Binance REST API`s (com+testnet, 
  com-margin+testnet, com-isolated_margin+testnet, com-futures+testnet, us, tr) in a simple, fast, flexible, robust 
  and fully-featured way. 
- [`UNICORN Binance Trailing Stop Loss`](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html): A Python SDK and [Command Line Tool](https://www.lucit.tech/ubtsl-cli.html) 
  from LUCIT with a trailing stop loss engine for the Binance Exchanges.
- [`UNICORN Binance WebSocket API`](https://www.lucit.tech/unicorn-binance-websocket-api.html): A Python SDK by LUCIT to use the Binance Websocket API`s (com+testnet, 
  com-margin+testnet, com-isolated_margin+testnet, com-futures+testnet, com-coin_futures, us, tr, dex/chain+testnet) in 
  a simple, fast, flexible, robust and fully-featured way. 
- [`UnicornFy`](https://www.lucit.tech/unicorn-fy.html): A Python SDK by LUCIT to convert received raw data from crypto exchange API endpoints into 
  well-formed python dictionaries. 

If you like our projects, please 
[![star](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-suite/master/images/misc/star.png)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/stargazers) them on 
[GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-suite)! 

## Get a UNICORN Binance Suite License

To run modules of the *UNICORN Binance Suite* you need a [valid license](https://technopathy.club/how-to-obtain-and-use-a-unicorn-binance-suite-license-key-and-run-the-ubs-module-according-to-best-87b0088124a8#4ca4)!

## Installation and Upgrade

The modules require Python 3.7 or above, as they depend on Pythons latest asyncio features for asynchronous/concurrent 
processing. 

For the PyPy interpreter we offer packages only from Python version 3.9 and higher.

[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

If you run into errors during the installation take a look [here](https://github.com/oliver-zehentleitner/unicorn-binance-suite/wiki/Installation).

### Packages are created automatically with GitHub Actions
When a new release is to be created, we start two GitHubActions: 

- [Build and Publish Anaconda](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/build_conda.yml)
- [Build and Publish GH+PyPi](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/build_wheels.yml) 

Both start virtual Windows/Linux/Mac servers provided by GitHub in the cloud with preconfigured environments and 
create the respective compilations and stub files, pack them into wheels and conda packages and then publish them on 
GitHub, PYPI and Anaconda. This is a transparent method that makes it possible to trace the source code behind a 
compilation.

### A Cython binary, PyPy or source code based CPython wheel of the latest version with `pip` from [PyPI](https://pypi.org/project/unicorn-binance-rest-api/)
Our [Cython](https://cython.org/) and [PyPy](https://www.pypy.org/) Wheels are available on [PyPI](https://pypi.org/), 
these wheels offer significant advantages for Python developers:

- ***Performance Boost with Cython Wheels:*** Cython is a programming language that supplements Python with static 
  typing and C-level performance. By compiling Python code into C, Cython Wheels can significantly enhance the 
  execution speed of Python code, especially in computationally intensive tasks. This means faster runtimes and more 
  efficient processing for users of our package. 

- ***PyPy Wheels for Enhanced Efficiency:*** PyPy is an alternative Python interpreter known for its speed and 
  efficiency. It uses Just-In-Time (JIT) compilation, which can dramatically improve the performance of Python code. 
  Our PyPy Wheels are tailored for compatibility with PyPy, allowing users to leverage this speed advantage seamlessly.

Both Cython and PyPy Wheels on PyPI make the installation process simpler and more straightforward. They ensure that 
you get the optimized version of our package with minimal setup, allowing you to focus on development rather than 
configuration.

#### Installation
`pip install unicorn-binance-suite`

#### Update
`pip install unicorn-binance-suite --upgrade`

### A Conda Package of the latest version with `conda` from [Anaconda](https://anaconda.org/lucit)
[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

The `unicorn-binance-suite` package is also available as a Cython version for the `linux-64`, `osx-64` 
and `win-64` architectures with [Conda](https://docs.conda.io/en/latest/) through the 
[`lucit` channel](https://anaconda.org/lucit). 

For optimal compatibility and performance, it is recommended to source the necessary dependencies from the 
[`conda-forge` channel](https://anaconda.org/conda-forge). 

#### Installation
[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

```
conda config --add channels conda-forge
conda config --add channels lucit
conda install -c lucit unicorn-binance-suite
```

#### Update
[There is no conda support until the migration to conda-forge.](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues/17)

`conda update -c lucit unicorn-binance-suite`

### From source of the latest release with PIP from [GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-suite)
#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-suite/archive/$(curl -s https://api.github.com/repos/LUCIT-Systems-and-Development/unicorn-binance-suite/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`

#### Windows
Use the below command with the version (such as 2.0.0) you determined 
[here](https://github.com/oliver-zehentleitner/unicorn-binance-suite/releases/latest):

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-suite/archive/2.0.0.tar.gz --upgrade`

### From the latest source (dev-stage) with PIP from [GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-suite)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-suite/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://www.python.org)
Download the [latest release](https://github.com/oliver-zehentleitner/unicorn-binance-suite/releases/latest) 
or the [current master branch](https://github.com/oliver-zehentleitner/unicorn-binance-suite/archive/master.zip)
 and use:
 
- ./environment.yml
- ./pyproject.toml
- ./requirements.txt
- ./setup.py

## Change Log
[https://oliver-zehentleitner.github.io/unicorn-binance-suite/changelog.html](https://oliver-zehentleitner.github.io/unicorn-binance-suite/changelog.html)

Please look for the information in the README.md of the [responsible subrepository](https://github.com/oliver-zehentleitner/unicorn-binance-suite#modules-of-the-unicorn-binance-suite).

## Documentation
- [General](https://oliver-zehentleitner.github.io/unicorn-binance-suite/)

Please look for the information in the README.md of the [responsible subrepository](https://github.com/oliver-zehentleitner/unicorn-binance-suite#modules-of-the-unicorn-binance-suite).

## Howto
- [How to Obtain and Use a Unicorn Binance Suite License Key and Run the UBS Module According to Best Practice](https://technopathy.club/how-to-obtain-and-use-a-unicorn-binance-suite-license-key-and-run-the-ubs-module-according-to-best-87b0088124a8)

## Project Homepage
[https://github.com/oliver-zehentleitner/unicorn-binance-suite](https://github.com/oliver-zehentleitner/unicorn-binance-suite)

## Wiki
[https://github.com/oliver-zehentleitner/unicorn-binance-suite/wiki](https://github.com/oliver-zehentleitner/unicorn-binance-suite/wiki)

## Social
- [Discussions](https://github.com/oliver-zehentleitner/unicorn-binance-suite/discussions)
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://community.binance.org](https://community.binance.org)

Please look for the information in the README.md of the [responsible subrepository](https://github.com/oliver-zehentleitner/unicorn-binance-suite#modules-of-the-unicorn-binance-suite) for spezific notifications.

## How to report Bugs or suggest Improvements?
Please look for the information in the README.md of the [responsible subrepository](https://github.com/oliver-zehentleitner/unicorn-binance-suite#modules-of-the-unicorn-binance-suite).

## Contributing
Please look for the information in the README.md of the [responsible subrepository](https://github.com/oliver-zehentleitner/unicorn-binance-suite#modules-of-the-unicorn-binance-suite).

## Disclaimer
This project is for informational purposes only. You should not construe this information or any other material as 
legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, 
endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in 
this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such 
jurisdiction.

### If you intend to use real money, use it at your own risk!

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities 
of any kind, including but not limited to direct or indirect damages for loss of profits.

### SOCKS5 Proxy / Geoblocking
We would like to explicitly point out that in our opinion US citizens are exclusively authorized to trade on Binance.US 
and that this restriction must not be circumvented!

The purpose of supporting a SOCKS5 proxy in the UNICORN Binance Suite and its modules is to allow non-US citizens to 
use US services. For example, GitHub actions with UBS will not work without a SOCKS5 proxy, as they will inevitably run 
on servers in the US and be blocked by Binance.com. Moreover, it also seems justified that traders, data scientists and 
companies from the US analyze binance.com market data - as long as they do not trade there.
