---
tags:
  - security
---
A collection of two CVEs chained to allow for priviledge escalation via Kerberos [[Priviledge Attribute Certificate|PAC]].
- [[CVE-2021-42287]]
- [[CVE-2021-42278]]
# Process
1. Change [[SamAccountName]] of computer account to name of domain controller (without the \$)
2. Request a [[Ticket Granting Ticket|TGT]] for the created computer account, once granted, change name of computer account back to original value
3. Request a [[Ticket Server|TGS]] for the [[Lightweight Directory Access Protocol|LDAP]] service, because there is no account with that name, TGS appends a \$ to it, then access to the service is granted and DA is acquired