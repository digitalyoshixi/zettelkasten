---
tags:
  - reverse_engineering
---
First check the filetype `file filename`  
# [[Executable and Linkable Format|ELF]] 
1. [[Fireeye Labs Obfuscated String Solver|FLOSS]]
2. `strace ./filename` (See [[strace]])
3. `ltrace ./filename`
4. `objdump -d ./filename`
5. [[Symbolic Execution]]
6. [[Ghidra]]
7. https://ide.kaitai.io/
# [[Portable Executable|PE]]
1. [[Ghidra]]