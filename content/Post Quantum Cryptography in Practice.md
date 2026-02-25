---
tags:
  - security
---
A talk at [[Toronto Area Security Klatch|TASK]]
# Notes
- [[RSA]], [[Diffie Hellman Key Exchange|DHKE]], [[Elliptic Curve Cryptography|ECC]] are all vulnerable to [[Shor's Factoring Algorithm|Shor's Algorithm]] ([[Discrete Logarithm Problem|DLP]], [[Elliptic Curve Discrete Logarithm]])
- [[Grover's Algorithm]] attacks [[Symmetric Cryptography]], not as important as [[Shor's Factoring Algorithm|Shor's Algorithm]]
- Shors will always convert to polynomial time
- Grovers search will reduce security level of symmetric crypto. But, you can increase the key size of symmetirc crypto and it usually will be safe
- Grover's search increases the speed of the algorithm by a quadratic factor
- [[Harvest Now Decrypt Later]], no quantum computers at the moment, but future we will have
- 