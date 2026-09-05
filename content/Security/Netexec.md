---
tags:
  - security
  - windows
aliases:
  - nxc
---
A tool to execute any code remotely from the internet
# Installation
- https://www.netexec.wiki/
# Usage
### Password Spray
```
nxc smb ips.txt -u usernames.txt -p 'p@ssword'
```
### Read LDAP
```
nxc ldap $DC -u $USER -p $PASSWORD
```
### Read SMB Data
```
nxc smb $DC -u $USER -p $PASSWORD
```