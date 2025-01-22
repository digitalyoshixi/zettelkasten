---
tags:
  - os
---
A process created by another parent process. Usually created from the `fork()` [[Syscall]].
They can inherit certain attributes from their parent process.
Usually they will either:
- Call back to the parent process
- Self-terminate
- Become a [[Orphan Process]]
- Become a [[Zombie Processes]]