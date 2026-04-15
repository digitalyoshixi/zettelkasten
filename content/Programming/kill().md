---
tags:
  - os
  - programming
  - c
aliases:
  - C kill()
---
A function used to invoke a [[Signal]] into any [[Process]]
```c
int kill(int pid, int signal)
```
- Returns 0 on success
- Returns non-negative if fail