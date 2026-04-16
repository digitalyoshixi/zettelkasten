---
tags:
  - programming
  - os
aliases:
  - waitpid
  - C waitpid()
---
[[wait()|wait]], but we wait for a specific child.
```c
pid_t waitpid(pid_t pid, int *status, int options);
```
- Process wants to block when no child has terminated
- Status have the exit status of the child written to it
- Options explains how to wait
	- If option is 0, waitpid blocks like [[wait()]]
	- If option is `WNOHANG`, it immediately returns 0 instead of blocking if there is no existing terminated child
- Returns process of waited child on success, -1 on failure