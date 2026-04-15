---
tags:
  - programming
  - os
aliases:
  - Little Endian
  - Big Endian
---
The little endian breaks their egg on the smaller side. The big endian breaks their egg on the larger side.
It works similarly to an egg. But the fluids are memory instead.
- Networks require big endian
- Memory is *usually* represented in little endian
### Little endian
- The [[Least Significant Bit|LSB]] is stored first (leftmost)
- The [[Most Significant Bit|MSB]] is stored last (rightmost)
![[Endness-20250708160310332.webp|189]]
Often preferred because it makes [[Binary Addition]], [[2's Complement|Binary Subtraction]] and address reading easier.
### Big endian
- The [[Most Significant Bit|MSB]] is stored first (leftmost)
- The [[Least Significant Bit|LSB]] is stored `last (rightmost)
![[Endness-20250708160232230.webp|197]]
Often used to transfer data over to network