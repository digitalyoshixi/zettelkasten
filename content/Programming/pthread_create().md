---
tags:
  - programming
  - os
---
```c
int pthread_create(pthread_t *tid, pthread_attr_t *attr, void *(*func)(void*), void *arg);
```
- Updates `tid` to be the thread within a process
- `attr` sets attributes like priority, stack size
	- Can set to `NULL` to get defaults
- `func` to call to start the thread
- `arg` is argument to `func`
- Returns 0 if successful, positive error code if not, does not set [[errno]], you can use [[strerror()]] instead