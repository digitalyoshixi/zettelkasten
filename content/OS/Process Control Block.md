---
tags:
  - os
  - scheduling
aliases:
  - PCB
---
![[Process Control Block-20260211163442156.webp]]
A segment of a process that includes:
- Process state. Is it running, waiting, terminated?
- [[Process ID|PID]]. Special identifier for this process
- Program counter. Tells us the current line of code being executed
- Registers. Tells us the memory address
- Memory limits. Represents memory currently being used
- [[Process Scheduling]]. Automating tasks
- [[File Descriptor Table]]
- Accounting information. Keeps accounts like info being used, time, memory.
- I/O status information. Tells us what I/O devices are assigned to this process.
- [[Signal]] table to point to segment of codes that will be executed once given signals are recieved