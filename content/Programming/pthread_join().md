---
tags:
  - programming
  - c
---
```c
int pthread_join(pthread_t tid, void **status);
```
Waits for the thread to terminate,
- `tid` is the thread to wait for
- `status` if not `NULL` returns the `void*` returned by the thread when it terminates
- Returns 0 on success, error number on error