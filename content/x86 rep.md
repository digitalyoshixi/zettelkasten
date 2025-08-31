---
tags:
  - programming
  - x86
  - assembly
---
A prefix for string instructions.
For every repetition:
- Increment [[rdi]]
- Increment [[rsi]]
- Subtract [[rcx]]
Until [[rcx]] is 0.