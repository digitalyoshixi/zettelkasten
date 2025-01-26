---
tags:
  - reverse_engineering
  - c
---
# C
Function to put characters to standard out. Requires [[stdio.h]]
```c
int puts(const char *str);
```
Example usage:
```c
#include <stdio.h>

int main(int argc, char *argv[]){
  puts("hello");
  return 0;
}

```
# [[x86 Assembly]]
Takes the value of edi and then outputs it to standard out
![[puts-20250108010405476.webp]]