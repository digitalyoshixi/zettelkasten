---
tags:
  - security
  - cryptography
---
A method of building [[Hash Collision]] resistant function.
Alternative to [[Sponge Construction]]
# Construction
- Message $M$ split into fixed length blocks. $M=m_{0}||m_{1}||\dots||m_{t}$
- Message blocks compressed one after another using a [[Compression Function]] $f$ to produce chaining variable $h_{i}$ that is used to compress $m_{i+1}$
- In other words, [[Compression Function]] $f(m_{i}, h_{i-1}) = h_{i}$
- $h_{0}$ is a fixed constant
![[Merkle Damgard Construction-20260219012325871.webp]]