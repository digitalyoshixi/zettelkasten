---
tags:
  - programming
  - security
---
These are gadgets that can be used to store addresses into registers.
1. Find a [[x86 lea]]
2. Find a `push rsp; pop rax; ret` - equivalent to `mov rax, rsp`
3. Find a `add rax, rsp; ret`
4. `xchg rax, rsp; ret` - swaps rax and rsp - DANGEROUS