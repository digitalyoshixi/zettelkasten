---
tags:
  - compilers
aliases:
  - AOT Compilation
---
Converts the entire source-code into [[Bytecode]] before runtime.
# Structure
![[Ahead-of-time Compilation-20251020153533467.webp]]
1. [[Tokenizer]]
2. [[Parser|Syntactic Analysis]]
3. [[Semantic Analysis]] ([[Checker]])
4. [[IR Generation]]
5. [[Decompiler Procedure Analyzer|CFG Analyzer]]
6. [[Machine Independent Optimizer]]
7. [[Codegen]]
8. [[Machine Dependent Optimization]]