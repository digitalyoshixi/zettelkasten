---
tags:
  - os
  - security
  - memory
---
The laundry pile of memory chunks
- When you free, and it doesn't fall in [[Tcache Bin]] or [[Fast Bin]], it goes here (When a [[Heap Chunk]] is freed, we don't immediately want to [[Chunk Coalescing|Coalesce]] it)
- Doubly circular list