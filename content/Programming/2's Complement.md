---
tags:
  - c
  - math
---
The most common method of representing signed integers.
![[2's Complement-20240130211858750.webp|452]]
### Key Concepts
- It uses the most significant bit to indicate whether the number is positive or negative
	- 1 is negative
	- 0 is positive
- Reading negative numbers is entirely different than reading positive numbers
It replaces [[Signed Magnitude Method]]

# Positive Numbers
Positive numbers are represented the exact same as in [[Signed Magnitude Method]]

# Negative Numbers
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

### Reading Negative Numbers
`101101`
First, know the MSB is negative, then add all the other bits
so that would be: -(2^5) + (2^3) + (2^2) + (2^0) = -32 + 8 + 4 + 1 = -19