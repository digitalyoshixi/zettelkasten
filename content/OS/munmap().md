---
tags:
  - os
---
```c
int munmap(void *addr, size_t len);
```
unmaps a region of memory starting from addr all the way to addr+len.
- Returns 0 if success
- Returns -1 if fails