---
tags:
  - math
  - cryptography
aliases:
  - PRNG
---
A random number generated from [[Deterministic Algorithm]].
# Implementations
### Linear Recursion
- [[Linear Congruential Generator|LCG]]
- [[Mersenne Twister]]
- [[xorshift]]
- [[Well Equidistributed Long-period LInear]]
### Counter-Based
$\text{output} = f(n,key)$
- [[Philox]]
- [[Threefry]]
### Secure PRNGs
- [[Block-Cipher]] in counter mode or output feedback mode
- [[Stream-Cipher]]