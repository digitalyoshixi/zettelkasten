---
tags:
  - c
  - math
aliases:
  - Binary Subtraction
---
The most common method of representing signed integers.
Designates the most significant byte to be the negative version of itself.
Is also equivalent to [[1's Complement]] + 1.
![[2's Complement-20250522155832356.webp]]
Replaces [[Signed Magnitude Method]]
# Computing Negative Numbers
Its a rather simple process
1. we have a positive number
![[2's Complement-20240130213541505.webp|568]]
2. flip each bit's polarity
![[2's Complement-20240130213612845.webp|552]]
3. Add one to the flipped value
![[2's Complement-20240130213633677.webp|549]]
4. Solve
![[2's Complement-20240130213651912.webp|561]]
5. The final negative value is
![[2's Complement-20240130213709922.webp]]
# Converting Unsigned to Signed
Simply Add $(+1)$ to the unsigned number, but ensure the sum is the same bit-width.
![[2's Complement-20250522160209627.webp]]
![[2's Complement-20250522160320697.webp|282]]