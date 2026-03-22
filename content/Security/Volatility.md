---
tags:
  - forensics
---
A [[Memory Forensics]] RAM discovery tool.
# Installation
```
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
```
### [[Arch Linux]]
```
sudo pacman -S volatility3
```
# Usage
```
python3 vol.py -f <FILE> <PLUGIN_NAME> (<PLUGIN_OPTION>)
```
### Arch (Incorrect Perms)
```
vol
```