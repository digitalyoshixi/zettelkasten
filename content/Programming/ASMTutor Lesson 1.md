---
tags:
  - ASMTutor
  - x86
---

### Lesson 1 system out

Would you get it out of your system? Heres how its done:

eax = 4. Opcode 4 to invoke sys_write

ebx = 1. Tells us to write to standard out

ecx = memaddress. This is the memory address of wherever our mesage string starts

edx = length. Tells us how many bytes we must continue moving until its the end of the string

Interrupt 0x80
