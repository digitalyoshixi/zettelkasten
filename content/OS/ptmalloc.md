---
tags:
  - memory
---
Used in the [[C]] language.
Uses a [[Data Segment]] with [[brk()]] and [[sbrk()]] to manage memory

ptmalloc slices off bits of the [[Data Segment]] for small allocations and uses [[mmap()]] for large allocations