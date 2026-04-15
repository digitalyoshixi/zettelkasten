---
tags:
  - programming
  - os
---
A [[Syscall]] used to create a copy of a [[File Descriptor]].
```c
int dup2(int oldfd, int newfd)
```
- Returns non-negative integer if works
- Returns -1 on error