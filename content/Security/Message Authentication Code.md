---
tags:
  - security
  - cryptography
aliases:
  - MAC
---
A code used for integrity checks.
$$
\text{MAC} = \text{Hash}(M|s)
$$
- $M$ is the message
- $\text{Hash}$ is the hash funciton
- $s$ is the secret key
# Properties
- [[Non-Repudiation]] is not given
- [[Integrity]]
# Types
- [[Secret Prefix MAC]]
- [[Global Message Authentication Code|GMAC]]
- [[Cipher-Based Message Authentication Code|CMAC]]
- [[Hash-based Message Authentication Code|HMAC]]
- [[Universal Message Authentication Code|UMAC]]
- [[Poly1305]]