---
tags:
  - compilers
aliases:
  - Inline Expansion
---
Replaces a function call site with the body of the called function.
Similar to [[Macro Expansion]].
Can be used for obfuscation when combined with [[Function Outlining]]
# Example
![[Function Inlining-20251126001823240.webp]]
# Tradeoff
Excess inlining will cost significant storage space and performance cuts.
Minor inlining is beneficial.