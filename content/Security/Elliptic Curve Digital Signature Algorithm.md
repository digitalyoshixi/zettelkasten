---
tags:
  - security
  - cryptography
aliases:
  - ECDSA
  - ECC Signature
---
# ECC Signature
$(R,S,V)$:
- $R$ : X-point on [[Elliptic Curve]]
- $S$ : proof signer knows private key
- $V$ : Polarity of curve (positive or negative)
	- Either 0(27) or 1(28)
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
# Verification
Taking signed message and signature $(R,S)$
- $e = H(M)$
- $h = e[32:]$
- $c = s^{-1} \mod n$
- $R' = (h*c) * G+(r * c) * aG$
- $r' = R'.x$
- Check if $r' = = r$