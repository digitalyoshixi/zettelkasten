---
tags:
  - programming
  - compilers
aliases:
  - Bailing Out
  - JIT Penalty
---
Falling back to the [[Interpreter]] if a [[Just-in-time Compilation|JIT Compilation]] produced a wrong optimization that does not work.
If a function keeps bailing out, then JIT will no longer try and optimize that function.

Could cause slower performance if frequent deoptimizations occur