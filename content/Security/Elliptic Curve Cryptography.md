---
tags:
  - cryptography
  - math
aliases:
  - ECC
  - PKCS 13
---
A [[Public-Key Cryptography]] algorithm that uses [[Elliptic Curve]].
used for equations like:
$$
y^{2} \equiv x^{3} + ax + b
$$
You can think of them like a [[Hashing|Hash Function]].
Easy to compute, and well supported for [[Embedded Device|Embedded Devices]]

An [[Elliptic Curve]] to be used has key fields:
- [[Generator Point]]
- [[Generator Order]]
# Implementations
- [[Elliptic-Curve Diffie Hellman Ephemeral|ECDHE]]
- [[Elliptic Curve Digital Signature Algorithm]]
- [[Schnorr's Signature]]
# Hard Problems
- [[Elliptic Curve Discrete Logarithm Problem]]
# Concepts
- [[Elliptic Curve]]