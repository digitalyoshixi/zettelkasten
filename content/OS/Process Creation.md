---
tags:
  - os
---
A process may occasionally create a child process. All child processes have the same traits as a regular process like process id and process registers and can make their own children.

When a process makes a child there are 2 possibilities:
1. The parent continues to execute concurrently with the child 
2. The parent waits for the children to terminate.

Additionally, for the address space: child processes canshare data with the parent process, or have new data loaded into it.

[[Process Termination]]