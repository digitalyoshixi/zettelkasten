---
tags:
  - os
  - security
  - reverse_engineering
---
This is a program used by a [[Decompiler]] to extract information from a [[Structured Object File Format]].
Attempts to acquire:
- Global variables
- Global functions
- [[Imports]] / Dynamically linked [[Imports]]
- [[Relocation|Relocation Table]]
- Export table (if the file is a [[Dynamic Linked Library|DLL]])
- If compiled with [[Debugging Information]]