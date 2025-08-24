---
tags:
  - python
---
A adoption of [[Docker]] to set local environments to use different python versions.
# Installation
### Arch
1. `sudo pacman -S pyenv`
2. Then `pyenv init`. follow the instructions
### [[Fedora Linux]]
1. `sudo yum install zlib zlib-devel bzip2-devel openssl-devel sqlite-devel readline-devel -y`
2. `curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash`

# Utilization
### Installing Different Python Version
```
pyenv install 3.10.4
```
### Listing Versions
```
pyenv versions
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