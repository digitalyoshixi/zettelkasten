---
tags:
  - programming
  - os
aliases:
  - exec
---
A [[Syscall]] used to replace the current process with another.
Replaces the [[Process Control Block|PCB]] open file descriptors with a different value.
```c
exec()
```
- On success, does not return
- On failure, returns -1
Keeps:
- [[Process ID|PID]], [[Parent Process ID]], [[Signal]] table