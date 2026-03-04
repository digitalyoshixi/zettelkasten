---
tags:
  - programming
  - os
---
A function that waits until a process finishes.
```c
pid_t wait(int wstatus)
```
# Example
```c
pid_t child_pid, wpid;
int status = 0;

//Father code (before child processes start)

for (int id=0; id<n; id++) {
    if ((child_pid = fork()) == 0) {
        //child code
        exit(0);
    }
}

while ((wpid = wait(&status)) > 0); // this way, the father waits for all the child processes 

//Father code (After all child processes end)

```