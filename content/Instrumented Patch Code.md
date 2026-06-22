---
tags:
  - security
---
Direct modification of the binary to your instrumented code in a linked library.
# Instrumentation
![[Trampoline Code-20260622022632840.webp|809]]
- Make sure the instrumented function restores register state & does appropriate execution calls as the original does
- Most often, the jmp that replaces takes 5-bytes, [[Interrupt 3]] takes 1 bytes