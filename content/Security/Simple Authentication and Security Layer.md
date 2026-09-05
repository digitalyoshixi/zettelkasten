---
tags:
  - windows
  - security
aliases:
  - SASL
---
A authentication mechanism that extends authentication for [[TCP & IP Application Layer|Application Layer Protocols]] ([[Lightweight Directory Access Protocol|LDAP]], [[Internet Message Access Protocol|IMAP]], [[Simple Mail Transfer Protocol|SMTP]], etc).
- Note that LDAP has its own authorization protocol built in
# Mechanisms
- `PLAIN` : Send username/password over plaintext
- `CRAM-MD5` : Challenge-response
- `DIGEST-MD5` : Stronger challenge response
- [[Generic Security Services Application Programming Interface]] : Use kerberos tickets for auth
- `EXTERNAL` : Use TLS certificates
- `NTLM` : Use [[New Technology LAN Manager|NTLM]]
- 