---
tags:
  - x86
  - ASMTutor
  - networking
  - syscall
---
### Lesson 31 socket listen

Requires a pointer to the array of arguments from lesson 30 as the only non-constant. Much easier

eax is 102

ebx is 4

ecx is stack pointer to array that includes value of ip address, port, 2 argument length and some more