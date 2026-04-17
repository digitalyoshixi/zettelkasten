---
tags:
  - os
  - linux
---
[[Signal]] 20.
Automatically called when a child exits.
# Example Signal Handler
```c
void sigchld_handler(int sig) {
  // Use waitpid() with WNOHANG to reap children
  int status;
  int pid;
  while ((pid = waitpid(-1, &status, WNOHANG)) > 0) {
    if (WIFEXITED(status)) write(2,"reaped\n", 7);
    else perror("statusexit\n");
  } 
}
```