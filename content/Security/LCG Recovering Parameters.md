---
tags:
  - cryptography
  - security
---
# Process
For a [[Linear Congruential Generator|LCG]] defined as $S_{n+1} = a S_{n}+b \mod m$
### Recovering m
- Define $t_{n} = S_{n+1} - S_{n}$
- $u_{n} = |t_{n+2} *t_{n} - t^{2}_{n+1}|$
- $m = gcd(u_{1},\dots,u_{k})$, usually $k \geq 10$
### Recovering a
- Recover $a$ as $t_{i} =  a\cdot t_{i-1} \mod m$
### Recovering c
- Recover $c$ as $S_{i+1} = a \cdot S_{i}+c \mod m$