---
tags:
  - os
  - memory
aliases:
  - Wilderness
---
A fake [[Heap Chunk]] representing the unused memory in a thread-local heap.
If there is no more room in the top chunk, [[glibc malloc]] will increase the size of the top chunk
![[Top Chunk-20260129222517766.webp]]