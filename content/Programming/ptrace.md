---
tags:
  - programming
  - os
---
A [[Syscall]] used to observe and control another process.
Used to implement debugging, breakpoints and system call tracing.
# Antidebugging
```c
// compile with gcc -o selfptrace selfptrace.c
#include <sys/ptrace.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if (ptrace(PTRACE_TRACEME,0) < 0) {
        printf("I am traced");
        exit(1);
    }
    printf("I am not traced");
    return 0;
}
```