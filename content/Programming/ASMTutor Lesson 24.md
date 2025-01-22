---
tags:
  - x86
  - ASMTutor
  - syscall
---
### Lesson 24 File opening (sys_unlink)

To “open”(get file descriptor), another syscall, ya already know.

eax as 5

ebx as memory location for filename

ecx as 0, 1 or 2 for readonly, write only or readwrite mode