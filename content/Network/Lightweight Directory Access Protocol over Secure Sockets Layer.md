---
tags:
  - security
aliases:
  - LDAPS
---
The secure version of [[Lightweight Directory Access Protocol|LDAP]] that uses [[Transport Layer Security|TLS]].
Runs on `tcp/636`
# Enabling
1. Require a [[Certificate Authority|CA]] server and a [[Domain Controller|DC]] server
2. On domain controller open certificate store: `certlm`
3. On [[Certificate Authority|CA]], generate a new certificate with Certification Authority `certsrv.msc`
4. Open `certtmpl.msc` > Kerberos Authentication > Duplicate Template > General > Rename to LDAPS > Publish Certificate in Active Directory > Request Handling > Allow private key to be exported
5. {domain} > Certificate Template > New 