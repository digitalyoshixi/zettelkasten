---
tags:
  - ASMTutor
  - x86
  - syscall
---
### Lesson 20 Forking hell

Fork you! All you require to fork a process is:

eax as 2

  

Very simple, no added arguments. To check if a process is a child, parent or failed, look at the register eax.

If eax < 0, error during fork

if eax = 0, child process

if eax > 0, parent process