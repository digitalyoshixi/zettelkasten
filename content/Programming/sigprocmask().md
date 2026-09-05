---
tags:
  - programming
  - c
aliases:
  - C sigprocmask()
---
```c
int sigprocmask(int how, const sigset_t *set, sigset_t *oset);
```
- Indicates how a signal should be modified
	- `SIG_BLOCK`: add to currently blocked
	- `SIG_UNBLOCK`: delete from currently blocked
	- `SIG_SETMASK`: set collection of signals from being blocked