---
tags:
  - programming
  - os
aliases:
  - wait
  - reap
---
A function that;
- Suspends execution until one of the child processes terminates
- Returns early if there is already a PID of a terminated child
```c
pid_t wait(int* status)
```
- Returns the [[Process ID|PID]] of the child or `-1` if there are no child processes
- Writes to the status the [[exit()]] status of the child process
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
printf("%d", WEXITSTATUS(status)); // get the return code

//Father code (After all child processes end)
```
# Exit Macros
- [[WIFEXITED()]]
- [[WEXITSTATUS()]]