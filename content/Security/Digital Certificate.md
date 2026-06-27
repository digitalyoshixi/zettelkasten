---
tags:
  - security
aliases:
  - Certificate
  - X509 Certificate
  - X.509 Certificate
---
A document used to link a [[Public Key]] to an entity.
Often includes:
- Subject: Information about identity of its owner
- Issuer: Information about its issuer ([[Certificate Authority|CA]] for [[TLS Certificate]])
Certificates are stored on the local device with [[File Extension]] `.cer` or `.pem`
# Types
- [[TLS Certificate]]
- [[Email Certificate]]
- [[Self-Signed Certificate]]
# Concepts
- [[Certificate Authority|CA]]
- [[Subordinate Certificate Authority|SubCA]]
- [[Certificate Revocation List|CRL]]
- [[Online Certificate Status Protocol]]
- [[Certificate Signing Request]]
- [[Certificate Serial Number]]
- [[Subject Alternative Name Certificate]]
# Attacks
- [[ANS1 Attack X509 Certificate]]
- [[Multiple Common Name Attack]]
- [[PKCS10 Tunnel SQL Injection]]