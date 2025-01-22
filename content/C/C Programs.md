---
tags:
  - c
---
All a program is is just a set of individual function definitions.
Function definitions do **NOT** have to be in the same file.

# Compiling
Again, its architecture dependant.
### GCC
`gcc file1.c file2.c file3.c`
and they will all compile to `a.out`
or 
`gcc -o myprogram file1.c file2.c file3.c`

### Example
```c
//programfir.c
#include <stdio.h>


int main(){
    int mygotten = getnum();
    printf("%d",mygotten);
    return 0;
}
```
```c
//programsec.c
int getnum(){
    return 20;
}
```
`gcc -o programtest programsec.c programfir.c`
this will give an error, but running the program should print `20`
