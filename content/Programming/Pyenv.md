---
tags:
  - python
---
A adoption of [[Docker]] to set local environments to use different python versions.
# Installation
1. `sudo pacman -S pyenv`
2. Then `pyenv init`. follow the instructions
# Utilization
### Installing Different Python Version
```
pyenv install 3.10.4
```
### Using Different Python Version
for global shell:
```
pyenv global 3.10.4
```
for current folder:
```
pyenv local 3.10.4
```
### Uninstall Python Version
```
pyenv uninstall 3.10.4
```