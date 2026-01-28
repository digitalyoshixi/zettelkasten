---
tags:
  - os
---
```
void *mmap(void *addr, size_t len, int prot, int flags, int fildes, off_t off);
```
A [[Syscall|System Call]] that is commonly used for:
- Creating pages in memory
- Mapping files into an address space of the program
Has a maximum of 4096 bytes that can be allocated