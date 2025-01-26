---
tags:
  - c
---
Strings are just an array of characters
![[C Strings-20240129223954945.webp]]
They always end with `\0`
so when you do something like `printf("%s", "sex")` it assumes your string ends with a null terminator.

### Initialization
```c
char mystr[] = "balls";
// or alternatively
char mystr2[] = {'f','a','g','\0'};
// or declare with fixed length
char mystr3[60];
mystr3 = "penis";
```
Yes, strings have a special initialization specifically for them which is `""`, how special!
# Methods
- [[strlen]]