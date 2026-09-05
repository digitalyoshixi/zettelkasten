---
tags:
  - security
aliases:
  - EKU
---
A collection of properties outlining what a [[Digital Certificate|X509 Certificate]] can be used for.
Listed as [[Object Identifier|OID]] in [[Windows Active Directory|AD]] as of Windows Server 2019.
# Typers
- `Server Authentication` : Certificate can be used to secure websites with [[Hyper Text Transfer Protocol Secure|HTTPS]]
- `Client Authentication` : Certificate can be used to prove who they are to a system
- `Smart Card Logon` : Certificate for system to allow smart card logon
- `PKINIT Client Authentication` : Used for [[Kerberos]] pre-auth
- `Secure Email (S-MIME)` : Used for email signing/encryption
- `Code Signing` : Used for signing executables/drivers/scripts