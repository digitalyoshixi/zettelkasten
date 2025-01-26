---
tags:
  - c
---
A combination of [[Static Variables]] and [[Global Variables]].

When declared, they will be known to all functions in a program.
They will even be known for all other files.

So static variables persist only for one file, extern variables persist through multiple files.

The convention is to put all extern variables at the start of the source file
```c
#include <stdio.h>

extern int vara = 0;
extern int varb = 1231;

int main(){
	return 0;
}
```
Remember the [[K&R Rearrangement License]] to avoid logic errors.