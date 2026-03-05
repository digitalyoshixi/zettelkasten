---
tags:
  - programming
  - os
aliases:
  - fork
---
A [[Syscall]] that is able to make a copy of the current [[Linux Process]].
```c
pid_t fork(void)
```
- Returns `0` if process is a child process
- Returns new child's [[Process ID|PID]] if process is parent process
- May fail if there are no more processes that can be handed out
# [[Process Control Block|PCB]] Changes
- [[Program Counter Register|PC]] is the exact same as the parent process
- [[File Descriptor]] is exactly the same as the parent processes (Allows [[Pipe]] communications)
- [[Process ID|PID]] changed
- [[OS Stack|Stack]] is copied exactly same