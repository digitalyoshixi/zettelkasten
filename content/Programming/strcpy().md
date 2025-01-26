---
tags:
  - c
  - binary_exploitation
---
strcpy is prone to buffer overflows. Use [[strncpy()]] instead

`strcpy(putstr, recvstr)`
copy the recvstr values as the putstr value 
```c 
#include <string.h>

int main() {
{
char str1[20] = "C programming";
  char str2[20];

  // copying str1 to str2
  strcpy(str2, str1);
}
```
