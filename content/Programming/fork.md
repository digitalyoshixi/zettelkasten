---
tags:
  - programming
  - os
---
A [[Syscall]] that is able to make a copy of the current [[Linux Process]].
```
fork()
```
- Returns `0` if process is a child process
- Returns new child's [[Process ID|PID]] if process is parent process
# [[Process Control Block|PCB]] Changes
- [[Program Counter Register|PC]] is the exact same as the parent process
- [[Process ID|PID]] changed
- [[OS Stack|Stack]] is copied exactly same