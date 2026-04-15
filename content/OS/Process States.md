---
tags:
  - os
aliases:
  - Process Lifecycle
---
As a process is in execution, its state may change. The state is the current activity of the process:
- **New:** when the process is being created
- **Ready:** waiting to be assigned to a processor
- **Running:** instructions are being executed
- **Waiting/Blocked:** waiting for a signal or I/O operation
- **Terminated:** finished execution

Each process' [[Process Control Block]] block helps with this.
# Example Lifecycle
![[Process States-20260415192705511.webp]]
- [[GCC]] can be be running, wants to access a file but its being used, becomes blocked while it waits
- After file is read, [[GCC]] moves to ready state, will be running when a CPU core is available to run it
- After GCC instruction are performed, moved back to ready state, then continues execution after next CPU is ready