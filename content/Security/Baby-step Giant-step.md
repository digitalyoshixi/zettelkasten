---
tags:
  - cryptography
aliases:
  - BSGS
---
A [[Collision Algorithm]] that finds the same number between 2 sets to solve the [[Discrete Logarithm Problem|DLP]] which looks like:
$$a^x \equiv b \mod N$$
These 2 sets are created as follows:
1. Choose a random integer $k$
2. Create a set 'A' of all numbers $a,a^2,a^3,\dots,a^{k-1}$ 
3. Create a set 'B' of all numbers $ba^{-k},ba^{-2k},\dots,ba^{-rk}$ where rk > N
If the [[Discrete Logarithm Problem|DLP]] has a solution, then there should be a number common between sets A and B.