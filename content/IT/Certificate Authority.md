---
tags:
  - web
  - security
aliases:
  - CA
  - Root CA
---
A server that issues [[Digital Certificate]].
A self-hosted CA is responsible for creating the certificates for all devices in the network, including itself which would have a [[Self-Signed Certificate]].
Acts as a [[Root of Trust]].
Can have [[Subordinate Certificate Authority|Intermediate CA]] handle certificates for different protocols.
# TLS Certificate Authorities
For [[TLS Certificate|TLS Certificates]], group of organizations that issue include:
- Verisign
- Comodo
- [[LetsEncrypt]]
- More at https://www.ccadb.org/
Your browser should have a list of trusted CAs.
![[Certificate Authority-20240726040726839.webp]]