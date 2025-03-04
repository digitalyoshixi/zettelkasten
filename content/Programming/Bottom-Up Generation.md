---
tags:
  - compilers
aliases:
  - Reverse Right most Derivation
---
Starting with the final input result, then working backwards to achieve the root node, choosing when to flip [[Productions|Production Rules]] to reverse derivations
# Example
If we have the production rules:
![[Bottom-Up Parsing-20250101215144306.webp]]
We can show that `S -> aabcde` by using bottom-up parsing:
![[Bottom-Up Parsing-20250101215453678.webp]]