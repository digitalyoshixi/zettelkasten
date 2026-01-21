---
tags:
  - programming
  - os
---
A [[Syscall]] used to transfer data between [[File Descriptor]].
```
ssize_t sendfile(int out_fd, int in_fd, off_t *offset, size_t count)
```