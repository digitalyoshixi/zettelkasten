---
tags:
  - c
---
Concatenates 2 strings together.
`char* strcat(str1, str2)`
assumes str1 is large enough to hold the extra added bytes.
```c
char str1[100] = "ba";
char str2[4] = "lls";
strcat(str1,str2); // now str1 = "balls"
```