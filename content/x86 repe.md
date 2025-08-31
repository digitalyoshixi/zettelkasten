---
tags:
  - programming
  - x86
  - assembly
aliases:
  - x86 repz
---
A prefix for string instructions.
For every repetition:
- Increment [[rdi]]
- Increment [[rsi]]
- Subtract [[rcx]]
Until [[rcx]] is 0 or until [[Zero Flag|ZF]] is 1