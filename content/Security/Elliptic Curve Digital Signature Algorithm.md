---
tags:
  - security
  - cryptography
aliases:
  - ECDSA
  - ECC Signature
---
# ECC Signature
$(V,R,S)$:
- $V$ : 
# Algorithm
A signature algorithm that uses [[Elliptic Curve Cryptography|ECC]].
![[Elliptic Curve Digital Signature Algorithm-20260529013107079.webp]]

# Protocol
With:
- Private key $\alpha$
- Public key $A = \alpha G$
- Message $m$ to sign
He creates signature:
- hash $h$ of message $m$
- random number $k$
- $r$ = x coordinate of $kG | n|$
- Calculate signature $s = (h+r \alpha)k^{-1} | n|$
- Signature as $(r,s)$