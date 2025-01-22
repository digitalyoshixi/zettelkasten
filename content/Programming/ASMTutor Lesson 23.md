---
tags:
  - x86
  - ASMTutor
  - syscall
---
### Lesson 23 File modification (sys_write)

In order to modify a file, we must first create the file then write to our newly created file. Registers are:

eax as 4

ebx as file descriptor value

ecx as memory location of file contents

edx as bitsize for content to write

  

Notice that 4 is used in sys_write aswell, just like printing to stdout, but rather, we are writing to a file instead