---
tags:
  - os
  - scheduling
---

Every process is represented by a process control block(PCB). The PCB includes:

- Process state. Is it running, waiting, terminated?
- Process number/id. Special identifier for this process
- Program counter. Tells us the current line of code being executed
- Registers. Tells us the memory address
- Memory limits. Represents memory currently being used
- [[Process Scheduling]]. Automating tasks
- List of open files
- Accounting information. Keeps accounts like info being used, time, memory.
- I/O status information. Tells us what I/O devices are assigned to this process.