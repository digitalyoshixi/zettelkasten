---
tags:
  - compilers
aliases:
  - Inline Expansion
---
Replaces a function call site with the body of the called function.
Similar to [[Macro Expansion]].

# Tradeoff
Excess inlining will cost significant storage space and performance cuts.
Minor inlining is beneficial.