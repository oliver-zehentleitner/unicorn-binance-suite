# unicorn-binance-suite Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to 
[Semantic Versioning](http://semver.org/).

[Discussions about unicorn-binance-suite releases!](https://github.com/oliver-zehentleitner/unicorn-binance-suite/discussions/categories/releases)

[How to upgrade to the latest version!](https://oliver-zehentleitner.github.io/unicorn-binance-suite/readme.html#installation-and-upgrade)

## 2.1.0.dev (development stage/unreleased/unstable)
### Changed
- `meta.yaml`: switched conda deps from the legacy `lucit::` channel
  prefixes to conda-forge. Removed the leftover `channels:` and
  `dependencies:` blocks (they are `environment.yml` keys, not valid
  in `meta.yaml`). Dropped the stale "Anaconda Release"/"Anaconda
  Downloads" lucit badges. Re-embedded the current `README.md` into
  `about.description`.
- `environment.yml`: dropped the `lucit` and `defaults` channels and
  the `lucit::` prefixes on suite deps — conda-forge only.
- `SECURITY.md`: replaced the lucit.tech contact form with the GitHub
  Security Advisories private reporting URL.
### Removed
- `.github/workflows/build_conda.yml`: the conda-forge feedstock
  (`conda-forge/unicorn-binance-suite-feedstock`) now builds and
  publishes the conda package; no in-repo build is needed anymore.

## 2.1.0
### Added                                                                                                                                                                                                                                                                                                             
- `ubdcc` as suite dependency — `pip install unicorn-binance-suite` now includes the DepthCache Cluster                                                                                                                                                                                                               
- `llms.txt` for AI tool integration (ChatGPT, Claude, Copilot) with use-case routing and code examples                                                                                                                                                                                                               
- Expanded bug report template with hardware, OS, Python version and exchange dropdowns                                                                                                                                                                                                                               
- UBDCC added to `tools/get_versions_of_unicorn_packages.py`                                                                                                                                                                                                                                                          
### Changed                                                                                                                                                                                                                                                                                                           
- License: LSOSL → MIT                                                                                                                                                                                                                                                                                                
- Author: LUCIT Systems and Development → Oliver Zehentleitner                                                                                                                                                                                                                                                      
- GitHub URLs: LUCIT-Systems-and-Development → oliver-zehentleitner                                                                                                                                                                                                                                                   
- Python: minimum 3.8 → 3.9, added support up to 3.14                                                                                                                                                                                                                                                                 
- Unit tests now run on all supported Python versions (3.9-3.14)                                                                                                                                                                                                                                                      
- Dependency pins updated to current releases (UBWA ≥2.12.0, UBRA ≥2.10.0, UBLDC ≥2.12.1, UBTSL ≥1.3.0, UnicornFy ≥0.17.1)                                                                                                                                                                                            
- README rewritten with competitor comparison, architecture diagram, quick start examples and conda-forge install                                                                                                                                                                                                     
- build_conda.yml: updated runner OS and Python version                                                                                                                                                                                                                                                               
### Removed                                                                                                                                                                                                                                                                                                           
- LUCIT licensing dependency (`lucit-licensing-python`)                                                                                                                                                                                                                                                               
- Gitter references                                                                                                                                                                                                                                                                                                   
- LUCIT branding from all files    

## 2.0.0
### Added
- lucit-licensing-python

## 1.1.0
### Added
- unicorn-binance-trailing-stop-loss

## 1.0.2
Testing azure pipe

## 1.0.1
PYPI and Conda integration

## 1.0.0
Initial release.
