---
tags:
  - os
---
Processes terminate once the last line of code is executed. It does the following
- returns a status value on termination(usually an integer) to its parent process(via wait() system call).
- Deallocate all its resources like I/O devices or memory
- Kill itself using [[exit()]] system call

You can terminate a process through its parent process with a system call.

[[Process Creation]]