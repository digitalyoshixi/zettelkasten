---
tags:
  - x86
  - ASMTutor
  - networking
  - syscall
---
### Lesson 30 socket bind

Same principles as lesson 29, we use the stack in this syscall as well. The item in the stack will be our ip address and port. We also use the destination index register

eax is 102

ebx is 2

ecx is stack pointer to array that includes value of ip address, port, 2 argument length and some more

edi is file descriptor value

  

This is how ecx and edi are made:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivco_tmp_5daf40eb82bea474.png)