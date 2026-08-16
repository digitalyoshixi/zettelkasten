---
tags:
  - programming
  - os
---
A [[Allocator]] that re-uses objects of the same type to avoid [[Fragmentation]].
- Uses [[Slab]] and [[Slab Cache]]
- Allocation suitable to fit data of certain types or size are reallocated
- Cache does not free space immediately after use
![[Slab Allocator-20260816192545700.webp]]