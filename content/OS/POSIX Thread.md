---
tags:
  - programming
  - os
aliases:
  - pthreads
---
The most common thread package on [[Unix]] systems.
# Process
1. Thread is created with [[pthread_create()]] to run a function, or to continue main
2. Thread terminates by returning from the given function or from main or from calling [[pthread_exit()]] 3. [[pthread_join()]] used to reap the return value from thread
# Functions
- [[pthread_create()]]
- [[pthread_join()]]
- [[pthread_exit()]]
- [[pthread_detach()]]
- [[pthread_self()]]
# Example
```c
pthread_t thread_ID;
int fd = open("afile", "r");
int result = pthread_create(&thread_ID, NULL, myThreadFn, (void*)&fd);
if (result != 0) printf("%s", strerror(result));
```