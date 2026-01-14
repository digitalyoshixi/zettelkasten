---
tags:
  - c
aliases:
  - CLA
---
inside the main method, you can take a few arguments.
```c
int main(int argc, char *argv[])
```
`argc` will be how many arguments are given. arguments delimited by space ' '
`argv` is a array of strings. just index it normally

# Printing all arguments
The first argument will always be the file name
```c
#include <stdio.h>

int main(int argc, char *argv[]){
    for (int currarg = 0; currarg < argc; currarg++){

        for (int i = 0; argv[currarg][i] != '\0'; i++){
            printf("%c", argv[currarg][i]);
        }
        printf("\n"); // space between next argument
    }
    return 0;
}
```
![[C Command Line Arguments-20240201052657289.webp]]