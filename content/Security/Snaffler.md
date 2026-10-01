---
tags:
  - security
---
A tool that gets a list of windows computers from [[Windows Active Directory|AD]] and enumerates all files in those shares.
```
snaffler.exe -s -o snaffler.log
```
# Linux 
```
sudo apt install snaffler-ng
```
# Usage
```
snaffler-ng -u $USER -p $USERPASS -d domain.local
```