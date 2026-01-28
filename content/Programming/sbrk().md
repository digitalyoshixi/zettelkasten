---
tags:
  - programming
  - meta
---
A [[Syscall]] that managed [[Data Segment]]
```
sbrk(NULL)
```
- Returns end of data segment
```
sbrk(delta)
```
- Expands end of data segment by delta bytes