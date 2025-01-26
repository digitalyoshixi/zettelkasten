---
tags:
  - os
---
```
void *mmap(void *addr, size_t len, int prot, int flags, int fildes, off_t off);
```
A [[Syscall|System Call]] that is commonly used for:
- Mapping files into an address space of the program
