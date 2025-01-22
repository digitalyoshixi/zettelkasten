---
tags:
  - llvm
---
A block `%a` dominates another block `%b` if each of block `%b`'s predecessors are:
- block `%a`
- dominated by block `%a`
In other words: *every path from %b passes through %a*
![[Drawing 2024-12-31 12.55.32.excalidraw]]
# Domination and [[LLVM phi]] Declarations
The most dominating block (like `%loop_start`) in this case will hold all of the phi declarations.
![[LLVM Block Domination-20241231180818793.webp]]