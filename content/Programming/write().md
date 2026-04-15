---
tags:
  - programming
  - os
aliases:
  - C write()
---
A [[Syscall]] used to write things to a file stream.
Is a [[Atomic Operations|Atomic Operation]]
```c
ssize_t write(int fd, void buf[count], int count)
```