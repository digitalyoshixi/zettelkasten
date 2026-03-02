---
tags:
  - cryptography
  - math
aliases:
  - S Box
---
A lookup table mapping a byte to another byte.
- Aims to have high [[Encryption Confusion]]
![[Substitution Box-20260210160258636.webp|455]]
# Table Derivation
Involves taking [[Modular Inverses]] in a [[Finite Field]] $2^{8}$ then applying a [[Affine Transformation]]
Can be expressed as a high degree polynomial
$$
f(x)=5x^{fe} + 9x^{fd} + f 9x^{fb} + 25x^{f7} + f 4x^{e f} + x^{d f} + b 5 x^{b f} + 8fx^{7 f} + 63
$$
Apply input values `0x00` to `0xff` and the outputs are the table values