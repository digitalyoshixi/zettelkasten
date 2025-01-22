---
tags:
  - x86
  - ASMTutor
  - syscall
---
### Lesson 25 File reading (sys_read)

Now we officially open a file, we read this file. We require there be a bss variable for us to store the content of this file

eax is 3

ebx is file descriptor value

ecx is memory location of bss variable

edx is bitsize for content to read

  

sys read will change the value inside of the bss variable you give it to be the one inside bitsize given and the file