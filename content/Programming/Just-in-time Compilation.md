---
tags:
  - programming
  - c
  - cpp
aliases:
  - JIT Compilation
  - Run-time Compilation
---
A program that is compiled during execution time, rather than before execution.
Commonly used in tandem with [[Interpreter|Interpreters]].
- The code must be continuously analyzed during execution to identify which segment of the code is to be compiled ([[Code Monitor]])
- Optimizations can happen on the fly, certain code segments can be saved with [[Common Subexpression Elimination]]
# Concepts
- [[Code Monitor]]
- [[Common Subexpression Elimination]]
- [[Deoptimization]]
- [[Optimization Stub]]