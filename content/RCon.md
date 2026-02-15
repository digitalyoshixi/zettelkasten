---
tags:
  - cryptography
aliases:
  - Round Constant
---
A recursive function that generates a [[Column Vector]].
For a given round, we XOR the current vector with the current round constant column vector we get.
![[RCon-20260215213857114.webp]]
# Generation
![[RCon-20260215210241151.webp]]
- Note that this diagram above is all that is needed for AES-128's 11 rounds
$$
rcon_{i} = \left[\begin{array}{cc} 
rc_{i}\\ 
\text{0x0}\\
\text{0x0}\\
\text{0x0}\\
\end{array}\right]
$$
Round constant is generated with the recursive function:
$$
rc_{i} = \begin{cases}
rc(1) = 1\\ 
rc(i) =  2 \cdot rc(i-1) & \text{if } rc(i-1) < \text{0x80} \\
rc(i) = (2 \cdot rc(i-1) ) \oplus \text{0x11B} & \text{if } rc(i-1) \geq \text{0x80}
\end{cases}
$$
