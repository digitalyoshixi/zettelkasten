---
tags:
  - programming
  - c
---
```c
int signal(int signum, sighandler_t handler)
```
- Returns a signal result enum
	- `SIG_ERR`: means error
- Sets a signal to call a signal handler