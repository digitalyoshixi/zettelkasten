---
tags:
  - x86
  - ASMTutor
  - networking
  - syscall
---
### Lesson 29 socket create

We utilize the stack aswell as our registers in this interrupt.

eax is 102

ebx is 1

ecx is stack pointer value towards the value 2 followed by 1 and 6

This is how its done:  
![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivcm_tmp_3649550ed87ec75f.png)

Eax will then hold an integer file descriptor value. If eax is -1, then we got an error