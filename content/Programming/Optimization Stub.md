---
tags:
  - programming
  - compilers
---
A step within [[Just-in-time Compilation|JIT Compilation]] wherein segments of code that can have multiple types are compiled with each type as a stub.
![[Optimization Stub-20260207223750586.webp]]
JIT tries every type combination as a tree, and chooses the stub that works well for ths case.
