---
tags:
  - security
  - windows
  - active_directory
aliases:
  - AD Certificate Template
---
A template used to generate new certificates. Outlines:
- Validity period (expiry date, renewal date)
- Usage purposes ([[Extended Key Usage|EKU]])
- Cryptographic requirements (key size, allowed ciphers)
- Subject specifications
- Requester permissions
Can be defined with mutliple [[Subject Alternative Name Certificate|SAN]]