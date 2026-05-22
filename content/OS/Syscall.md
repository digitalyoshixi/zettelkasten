---
tags:
  - os
  - syscall
aliases:
  - Syscalls
  - System Calls
---
Calls made from [[Protection Ring|Userland]] to the [[IT/Operating System|OS]] to access [[Protection Ring|Kernel Level]] resources.
![[Syscall-20260522164326168.webp]]
# Syscall List
https://x86.syscall.sh/
You can view each syscall's with [[man]], like: `man open`
- [[open()]]
- [[exit()]]
- [[read()]]
- [[write()]]
- [[mmap()]]
- [[munmap()]]
- [[stat()]]
# System Call Errors
Syscalls will keep their error enum in [[errno]] that can be printed with [[perror()]]
# Resources
- https://www.felixcloutier.com/x86/
- https://syscall.sh/
- http://ref.x86asm.net/coder64.html