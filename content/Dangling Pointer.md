---
tags:
  - programming
  - c
---
A [[Memory Leak]] where you use a pointer that was previously freed.
Could cause [[Use After Free|UAF]].
```c
char *p = malloc(5);

```