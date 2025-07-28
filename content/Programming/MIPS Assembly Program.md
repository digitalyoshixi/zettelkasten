---
tags:
  - assembly
aliases:
  - MIPS Program Sections
---
The general structure of an assembly program should have:
- `.data` for all values
- `.text` for all assembly code
	- `.globl main` to make the main label visible to [[IT/Operating System|OS]]
	- `main:` to setup a main [[C labels|label]]
	- [[Microprocessor Without Interlocked Pipelined Stages Assembly|MIPS Assembly Instructions]]
	- [[Syscall]] at the end to signal program finish
![[MIPS Assembly Program-20250629165940859.webp]]
![[MIPS Assembly Program-20250708155030213.webp|410]]
# Example Program
![[MIPS Assembly Program-20250629165955355.webp]]
# Snippets
- [[MIPS Boilerplate Snippet]]
- [[MIPS Load Variable Snippet]]
- [[MIPS Array and For Loop Snippet]]
- [[MIPS 2D Loop Snippet]]