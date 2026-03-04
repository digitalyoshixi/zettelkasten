---
tags:
  - programming
  - os
aliases:
  - waitpid
---
A process wants to wait for its child.
```c
pid_t waitpid(pid_t pid, int *status, int options);
```
- Process wants to block when no child has terminated
- Option is 0, waitpid blocks like [[C Wait]]