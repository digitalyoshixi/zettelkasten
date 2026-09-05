---
tags:
  - security
  - windows
aliases:
  - Weak Explicit Certificate Mapping
---
A [[ADCS Privilege Escalation]] vulnerability that abuses any [[Active Directory altSecurityIdentities]] that are 'weak':
- Mapping to a common name like `X509:<S>CN=SomeUser`
- Using a generic DN `X509:<I>CN=SomeInternaCA<S>CN=GenericUser`
- Easily predictable identifiers an attacker can forge
# Requirements
- A weak [[Active Directory altSecurityIdentities]] that you can forge
# Identification
- [[Powershell]] `Get-ADUser -Properties altSecurityIdentities`
- [[Lightweight Directory Access Protocol|LDAP]] queries `altSecurityIdentities`
- [[Bloodhound]]
# Exploitation
1. Identify a weak mapping (i.e `X509:<S>CN=DAUserBackupCert`)
2. Obtain a matching certificate that satisfies criteria of this weak mapping
3. Authenticate as a target account