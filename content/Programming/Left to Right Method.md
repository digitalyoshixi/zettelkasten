---
tags:
  - math
  - programming
aliases:
  - L2R Method
  - Leftmost Derivation
---
A general process to construct a [[Control Flow Graph|CFG]].
1. Start with the root, and define the all left terminals and a variable for the right-end
2. Continuously fill in the non-terminal starting from left-side until the right-end is the same as a previously defined variable or a terminal
Grammars has the form:
```
A -> <terminals> <variables>
```
# Examples
- [[Finding CFG Example 2]]