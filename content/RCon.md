---
tags:
  - cryptography
aliases:
  - Round Constant
---
A constant matrix consisting of [[Column Vector]].
For a given round, we XOR the current vector with the current round constant column vector index
# Generation
![[RCon-20260215210241151.webp]]
Round constant is generated with the recursive function:
$$
\begin{cases}
rc(1) = 1\\ 
rc(i) =  2 \cdot rc(i-1) & \text{if } rc(i-1) < \text{0x80} \\
rc(i) = (2 \cdot rc(i-1) ) \oplus \text{0x11B} & \text{if } rc(i-1) \geq \text{0x80}
\end{cases}
$$
