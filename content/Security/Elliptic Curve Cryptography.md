---
tags:
  - cryptography
  - math
aliases:
  - ECC
  - PKCS 13
---
A [[Public-Key Cryptography]] algorithm that uses [[Elliptical Curves]].
used for equations like:
$$
y^{3} \equiv x^{3} + ax + b
$$
Easy to compute, and well supported for [[Embedded Device|Embedded Devices]]
# Implementations
- [[Elliptic-Curve Diffie Hellman Ephemeral|ECDHE]]
- [[Elliptic Curve Digital Signature Algorithm]]
# Problems
- [[Elliptic Curve Discrete Logarithm]]