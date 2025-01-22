---
tags:
  - ASMTutor
  - x86
  - networking
  - syscall
---
### Lesson 33 socket read

Once a connection is accepted, a new file descriptor is returned in eax, we can use this new file descriptor to read the request given.

We use the kernel function sys read and read up to 255 bytes.

Its also quite common to fork a child process to read for you. We keep the parent process to keep listening and accepting and the children will read.

eax is 3

ebx is socket file descriptor value

ecx is bss variable

edx is size of bss variable

  

After this program is run, send a curl command to localhost 9001. curl http://localhost:9001