---
tags:
  - cryptography
  - math
aliases:
  - MT
---
A [[Pseudo Random Number Generator|PRNG]] generator that involves using [[Mersenne Primes]] as its period length. Often uses prime $2^{19937}-1$
![[Mersenne Twister-20250722154943340.webp]]
# Algorithm
1. Define [[K Distribution]]
2. Given input seed of $w$-bit word length, mersenne twister generates integers in the range $[0, 2^{w}-1]$
3. Take input seed and initialize it, makes it a very large number
