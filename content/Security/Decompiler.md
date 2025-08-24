---
tags:
  - security
  - reverse_engineering
---
A tool that converts compiled binary [[Object File]] into source code
# Process
![[Decompiler-20250824021010905.webp]]
1. [[File Reader]]
2. [[Disassembler]]
3. [[IR Lifting]]
4. [[Decompiler Procedure Finder]]
5. [[Decompiler Procedure Analyzer]]
	1. [[Decompiler Expression Structuring]]
# Resources
- https://www.backerstreet.com/decompiler/expression_propagation.php
- https://mahaloz.re/dec-history-pt1
- https://decompilation.wiki/fundamentals/cfg-recovery/lifting/
- https://www.program-transformation.org/Transform/HistoryOfDecompilation2.html