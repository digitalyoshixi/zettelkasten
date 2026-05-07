---
tags:
  - windows
  - security
aliases:
  - ADCS
---
A service used to implement [[Public Key Infrastructure|PKI]] in [[Windows Active Directory|AD]].
# Discover ADCS servers
You can discover ADCS servers using [[Netexec]]
```
nxc ldap 192.168.56.10-23 -u '' -p '' -M adcs
```
