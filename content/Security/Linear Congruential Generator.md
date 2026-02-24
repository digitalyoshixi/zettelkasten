---
tags:
  - math
  - cryptography
aliases:
  - LCG
---
A very weak cryptographic algorithm created from pseudo-randomized numbers. 

$$X_{n+1}=(aX_{n}+c)\%m$$
$X_{n}$ is the previous number or the seed if this is the first item of the sequence, $0 < X_{0} < m$
$a$ is a randomly generated constant, $0 < a < m$
$c$ is a randomly generated constant, $0 \leq c < m$
$m$ is a randomly generated constant, $0 < m$

The LCG repeats itself. 634763476347634763476347. is a example output that it gives when $a=3,X_{n}=7,c=5,m=10$

# Breaking LCG
If m is known to the attacker, and a,b are not known, then you can break LCG.