---
tags:
  - os
  - meta
  - security
---
A thread-specific bin for small allocations.
- 64 bins - max count of 7, min size of 0x20, max size of 0x410
	- Subtract 8 for metadata, min-size for bin is 24 bytes or less
- [[Linked List|Singly Linked List]] (only forward pointers)
- Each new thread gets a new tcache