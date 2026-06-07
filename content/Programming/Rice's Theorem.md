---
tags:
  - programming
  - compilers
  - security
aliases:
  - Rices Theorem
---
All non-trivial semantic properties of a program are [[Undecidable]].
This means you must [[Software Verification|Verify]] programs on a case-by-case basis.
# Theorem
For any interesting property $Pr$ of the behavior of a program, it is impossible to write an analysis that can decide for every program $p$ whether $Pr$ holds for $p$.