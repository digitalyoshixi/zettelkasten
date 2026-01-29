---
tags:
  - security
  - binary_exploitation
---
Based on [[ptmalloc]] .
# Heap Creation
### Checking brk or malloc
1. If parent thread, and memory wanted exceeds [[C Macro]] `DEFAULT_MMAP_THRESHOLD`, then allocate with [[mmap()]]
2. Else, we setup with brk()
### Setup with brk()
- `End_data` : pointer that sets end of data segment
- `start_brk` : pointer that denotes beginning of heap
- `Brk / program break` : pointer that denotes end of heap segment
- [[brk()]] used to initialize `end_data` to the value specificied by addr
- `start_brk` set to next available segment after data segment
- `brk = start_brk`
- To expand/shrink dimensions of heap, [[sbrk()]] is used
![[glibc malloc-20260129054012303.webp]]
### Setup with mmap()
we mmap() things at the Memory Map Segment
![[glibc malloc-20260129054724218.webp]]