---
tags:
  - hardware
aliases: []
---
A [[Multiplier]] that follows [[Booth's Algorithm]] to simplify multiplications, making them faster.
# Algorithm
1. For multiplicants $A$ and $B$ being bytes with length $n$
2. With product being $P$, length of $2n$
3. Add an extra zero bit to the right-most side of $A$
4. Repeat for each original bit in A (not the zeroes on the left):
	1. If the last 2 bits of $A$ are the same, do nothing
	2. If the last 2 bits of $A$ are $01$, then add $B$ to highest bits of $P$
	3. If the last 2 bits of $A$ are $10$, then subtract $B$ from highest bits of $P$
	4. Perform [[Bitwise Right Shift]] on $P$ and $A$
### Example
![[Booth Multiplier-20250610193125751.webp]]
![[Booth Multiplier-20250610192948217.webp]]
![[Booth Multiplier-20250610193112182.webp]]
![[Booth Multiplier-20250610193151732.webp]]
![[Booth Multiplier-20250610193217701.webp]]
![[Booth Multiplier-20250610193310444.webp]]
![[Booth Multiplier-20250610193320834.webp|406]]