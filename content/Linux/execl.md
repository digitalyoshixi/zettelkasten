---
tags:
  - programming
  - os
---
A syscall used to execute another program.
```c
execl("program_filepath", arg1, ..., NULL)
```
- Takes in multiple argument strings terminated by `NULL`
Execl will only change the current process's data to be the one that is called. The process ID is the same. [[Program Counter Register|PC]] is reset.
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