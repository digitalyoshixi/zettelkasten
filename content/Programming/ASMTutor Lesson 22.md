---
tags:
  - x86
  - ASMTutor
  - syscall
---
### Lesson 22 File creation (sys_creat)

Let's make some uh files. We could execute commands like we did, but there are built in options in assembly to do this for us. This will be easier on memory so let's do that.

eax as 8

ebx as memory location for filename

ecx as file permissions linux style. 0777o for all permissions

Triggering the interrupt will then change eax to have the file descriptor value of the file created