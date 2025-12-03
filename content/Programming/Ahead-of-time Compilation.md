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
3. [[Semantic Analysis]]
4. [[Intermediate Representation|IR]] generation
5. [[Compiler Analysis]]
6. [[Machine Independent Optimizer]] and [[Dataflow Analysis]]
7. Machine dependent codegen
8. [[Machine Dependent Optimization]]