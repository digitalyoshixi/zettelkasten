---
tags:
  - programming
  - c
---
```c
void pthread_detach(pthread_tid tid);
```
- Detaches thread from running, cannot be tracked with [[pthread_join()]]
- Thread becomes a '[[Daemon Process|Daemon]]'