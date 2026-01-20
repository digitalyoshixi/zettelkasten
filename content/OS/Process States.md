---
tags:
  - os
---
As a process is in execution, its state may change. The state is the current activity of the process.

- New: when the process is being created
- Ready: waiting to be assigned to a processor
- Running: instructions are being executed
- Waiting: waiting for a signal or I/O operation
- Terminated: finished execution

When it starts running, it can either complete its operations, be interrupted or start waiting. If it gets interrupted, it will return to the ready state. If it must wait, then kills itself for a temporary while, while it waits for a signal, after which it returns to the ready state

Each process' [[Process Control Block(PCB)]] block helps with this