---
tags:
  - programming
  - os
---
```c
int dup(int fd)
```
A [[Syscall]] used to change entries in the [[Process Control Block|PCB]] file descriptor table by copying file descriptors into a free file descriptor in the file descritor table.
- Takes in the file descriptor to copy
- Returns the copied file descriptor number
