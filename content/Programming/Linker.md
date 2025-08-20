---
aliases:
  - Linking
tags:
  - c
  - cpp
banner:
---
After you have [[Compiler|Compiled]] your [[C]] program and are given object files, you are going to pass it through the linker.
# Process
The linker does 3 things:
1. Turns current object files and object files found within required libraries into an executable.
   ![[Pasted image 20231119140137.png]] 
2. Links object files
3. Resolves dependencies. The linker will abort if it detects errors in dependencies such as missing methods.
# Linking Types
- [[Static Linking]]
- [[Runtime Linking]]
- [[Dynamic Linking]]