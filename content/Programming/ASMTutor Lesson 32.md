---
tags:
  - x86
  - ASMTutor
  - networking
  - syscall
---
### Lesson 32 socket accept

To promote wench-like behavior, we must accept all offers.

eax is 102

ebx is 5

ecx is stack pointer to array that includes length, arguments and file descriptor

  

Accept creates a subroutine that will create a new file descriptor for the incoming socket connection.

The program will run continuously since it is listening. In another terminal, type “sudo netstat -plnt” to view the socket listening on port 9001