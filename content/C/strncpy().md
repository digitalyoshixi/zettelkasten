---
tags:
  - c
---
A more secure version of [[strcpy()]] which requires you to provide the # of bytes to be copied.

*Note: do not copy more than the length of the string. it will override the '\\0' null terminator*

```c
#include <stdio.h>
#include <string.h>

int main(){
    char str1[] = "HI MAN";
    char str2[7];

    strncpy(str2, str1, 6); // do not go over the length of str2
}
```