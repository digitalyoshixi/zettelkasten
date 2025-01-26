---
tags:
  - reverse_engineering
  - linux
---
# Reverse Engineering Process
1. `file`
	1. Determine architecture
	2. Determine if [[Stripped Binary]]
2. [[Fireeye Labs Obfuscated String Solver|FLOSS]]
	1. This is to find strings
3. `strace ./filename` (See [[strace]])
	1. Look at the [[Syscall]]
4. `ltrace ./filename`
	1. Look at what libraries are loaded and when
5. `readelf -a ./filename -M intel`
	1. Look for the entry point
6. `nm -a ./filename`
	1. Look at the functions in the program
7. `objdump -d ./filename -M intel`
	1. Look at the disassembly of the program
8. [[Symbolic Execution]]
9. [[Ghidra]]
10. https://ide.kaitai.io/
# Concepts
- [[Executable and Linkable Format|ELF]]
- [[Register]]
- [[Stack]]
- [[Heap]]
