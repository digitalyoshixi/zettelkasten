---
tags:
  - programming
  - os
---
A syscall used to execute another program.
```c
execl("program_filepath", arg1, ...)
```
Execl will only change the current process's data to be the one that is called. The process ID is the same.
It will no longer continue executing what was previously there.
# Example
```c
#include <stdio.h>
#include <unistd.h>
int main(){
	printf("about to call execl, PID: %d", getpid());
	execl("./hello", NULL);
	perror("exec");
	return 1;
}
```