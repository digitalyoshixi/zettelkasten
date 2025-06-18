---
tags:
  - hardware
aliases:
  - CLA
  - Fast Adder
---
A N-bit adder, that does not have high propogation delay.
- Uses [[PG Full Adder]]
We can get:
- $S = P_{i} \oplus C_{i}$
- $Carry = G_{i} + P_{i} \cdot C_{i}$
# 4 Bit Carry Unit
![[Carry-Look-Ahead Adder-20250617195513006.webp]]
# Block Diagram
![[Carry-Look-Ahead Adder-20250617200539558.webp]]
# Truth Table
![[Carry-Look-Ahead Adder-20250617194411737.webp]]