---
tags:
  - reverse_engineering
---
First check the filetype `file filename`  
# [[Executable and Linkable Format|ELF]] 
1. [[Fireeye Labs Obfuscated String Solver|FLOSS]]
2. `strace ./filename` (See [[strace]])
3. `ltrace ./filename`
4. `readelf -a ./filename -M intel`
6. `objdump -d ./filename`
7. [[Symbolic Execution]]
8. [[Ghidra]]
9. https://ide.kaitai.io/
# [[Portable Executable|PE]]
1. [[Ghidra]]