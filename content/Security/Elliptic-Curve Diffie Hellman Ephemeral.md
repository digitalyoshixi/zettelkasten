---
tags:
  - security
aliases:
  - ECDHE
---
This is an [[Elliptic Curve Cryptography]] algorithm for [[Key Exchange Protocol|Key Exchange]]
# Algorithm
![[Elliptic Curve Digital Signature Algorithm-20260529012002798.webp]]
- Bob picks a private key $a$
- Bob calculates a public key by multiplying $aG$ with their [[ECC Generator]] $G$
- Alice picks a private key $b$
- Alice calculates a public key by multiplying $bG$ with their [[ECC Generator]] $G$
- shared secret $S = ab$