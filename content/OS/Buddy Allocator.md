---
tags:
  - programming
  - os
---
A [[Allocator]] that divides memory into power-of-two partitions calls buddies.
- Block keeps splitting until required size is reached
- Freed buddies can merge back into larger blocks ([[Chunk Coalescing]])
# Example
To allocate 25KB, 128KB Block is split into 64KB then 32KB:
![[Buddy Allocator-20260816192020250.webp]]