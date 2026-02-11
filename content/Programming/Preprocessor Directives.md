---
aliases:
  - Compiler Directive
  - Macro
  - Precompiler Instruction
tags:
  - c
  - cpp
cssclasses:
---
lines preceded with a hash sign(#). these are special lines of code that the [[Preprocessor]] resolves before running other lines. They can be:
- [[Header File]] imports like `#include <iostream>`
- [[C++ Macros]]
- [[C++ Conditional Compilation]]
# Special properties
- You have NO semicolons after these.
- they are compiled TOP->BOTTOM. Scope does not matter
- They are file-local. Theyre discarded after compilation
