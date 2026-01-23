---
tags:
  - programming
  - os
---
A technique to allocate larger [[Heap Chunk]] by coalescing previously freed chunks into one big chunk.
# Process
1. Check the if the previous chunk was also freed, if it is, then check if their combined size can fit the requested size
2. Repeat