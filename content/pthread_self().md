---
tags:
  - programming
  - os
  - c
---
```c
pthread_t pthread_self(void)
```
- Returns thread id of thread that called it

Is often used with [[pthread_detach()]] to turn self into daemon.