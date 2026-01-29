---
tags:
  - os
  - security
  - memory
---
- The 'overflow' for [[Tcache Bin]]. If a tcache bin overflows, then we use a fast bin
- 10 bins, between 0x20 and 0xb0, sometimes only 7 are active
- In-use bit is maintained to prevent [[Chunk Coalescing]]
- [[Linked List|Singly Linked List]]