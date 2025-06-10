---
tags:
  - hardware
---
This is a [[Sequential Circuit|Sequential]] [[Multiplier]].
# Process
![[Accumulator Multiplier-20250610183711704.webp]]
1. Initialize $R = 00\dots 0$ as a [[Shift Register]]
2. You multiply each bit of $A$ by $B$, add it to $R$
3. Shift $R$ to the left by $1$ (It does this every clock cycle)
4. Repeat until each bit of $A$ is multiplied and added
# Block Diagram
![[Accumulator Multiplier-20250610183818757.webp]]

# Pros & Cons
### Pros
- Cheaper to build
### Cons
- Time complexity is $O(N)$