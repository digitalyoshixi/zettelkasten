---
tags:
  - c
---
in certain architectures, characters may be defined as to never be negative.
This means that when you are using char, the behavior may vary depending on architecture.

For example, if char is never negative and [[End of File|EOF]] is defined as `-1`, then you can never compare char to [[End of File|EOF]]

```c
char c;
c = getchar();
if (c == EOF) {} // will not happen if EOF is -1
```
the way to get around this is by using [[C Typecasting]] with char <-> int
```c
int c;
c = getchar();
if (c== EOF) {} // will happen now
```
**Note: there is no other reason for declaring char as int OTHER than getchar() which requires this oddly specific case**

