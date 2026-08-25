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
2. On [[Certificate Authority|CA]], generate a new certificate with Certification Authority, Open `certtmpl.msc` > Kerberos Authentication > Duplicate Template > General > Rename to LDAPS > Publish Certificate in Active Directory > Request Handling > Allow private key to be exported > Subject Name > DNS name enabled > Apply > OK
3. On CA, open `certsrv.msc` > Certificate Templates > New > Certificate Template to Issue > LDAPS > OK
4. On domain controller `gpupdate /force`, then open certificate store: `certlm` > Personal > All Tasks > Request New Certificate > Next > Active Directory Enrollment Policy > Next > LDAPS > Enroll > FInish