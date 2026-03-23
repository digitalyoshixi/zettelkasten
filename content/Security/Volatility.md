---
tags:
  - forensics
---
A [[Memory Forensics]] RAM discovery tool.
# Installation
```
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
pip install --user -e ".[full]"
```
# Concepts
- [[Volatility Symbol Tables]]
# Usage
```
python3 vol.py -f <FILE> <PLUGIN_NAME> (<PLUGIN_OPTION>)
```
### Windows Plugins
- [[Volatility Windows Viewing Dump Info]]
- [[Volatility Windows Viewing All Processes]]
- [[Volatility Windows Viewing All Open File Handles]]
- [[Volatility Windows Dump File]]
- [[Volatility Windows View Command Line Commands]]
- [[Volatility Windows View Netstat]]
- [[Volatility Windows Get Password Hashes]]
- [[Volatility Windows View Registry]]
### Extra
- [[Volatility View IDT]]