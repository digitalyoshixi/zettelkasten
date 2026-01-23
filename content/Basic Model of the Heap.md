---
tags:
  - os
  - security
---
![[Basic Model of the Heap-20260123035041300.webp]]
# Malloc
- Chunks of heap memory get seperated for a specific region that is allocated
- If you have a previously freed chunk (with similar size to what we are requesting), we re-use that same chunk
# Free
- A chunk is added to a free list
- 