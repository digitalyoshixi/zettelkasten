---
tags:
  - cryptography
  - security
aliases:
  - Sponge Function
---
An alternative to [[Merkle Damgard Construction]]. Using a function that can absorb and squeeze arbitrary size data.
# Construction
- With input $M = m_{1}||m_{2}||\dots||m_{n}$
- With hashed output $Z=z_{1}||z_{2}||\dots||z_{n}$
- With internal state comprised of $r$-bits (rate) and $c$-bits (capacity)
	- $c$ should be double the desired resistance to [[Hash Collision]] or [[Preimage Attack]]
![[Sponge Construction-20260219012707754.webp]]