---
tags:
  - c
---
`strstr(char str1[], char str2[])`
searches `str1` for the first instance of `str2`, then returns the pointer to `str2`.

```c
char str1[] = "vinegar";
char str2[] = "negar";
char *location = strstr(str1,str2);
```