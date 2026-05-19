---
tags:
  - windows
  - security
aliases:
  - ADCS
---
A service used to implement [[Public Key Infrastructure|PKI]] in [[Windows Active Directory|AD]].
# Issuing Protocol
![[Active Directory Certificate Services-20260507133245513.webp]]
- Client requests a [[Certificate Signing Request|CSR]] to [[Certificate Authority|CA]]
- The [[Certificate Authority|CA]] will request a [[Active Directory Certificate Template]] to be given so it can fill it out according to the certificate request
# Discover ADCS servers
You can discover ADCS servers using [[Netexec]]
```
nxc ldap 192.168.56.10-23 -u '' -p '' -M adcs
```