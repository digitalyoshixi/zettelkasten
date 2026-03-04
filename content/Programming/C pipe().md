---
tags:
  - programming
  - c
---
A function used to create a [[Pipe]].
```c
int fd[2]; // two arrays, fd[0] is read, fd[1] is write
pipe(fd);
```

![[Pipe-20260304010825785.webp]]