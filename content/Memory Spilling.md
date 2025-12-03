---
tags:
  - programming
  - compilers
---
A method to spill values of registers onto stack, then pop it back later.
Assists in [[Register Allocation]].
![[Memory Spilling-20251203023739438.webp]]
Has risks. Never spill:
- Loop iteration variables