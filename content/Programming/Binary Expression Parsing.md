---
tags:
  - llvm
  - compiling
---
These are expressions in the form of:
- `a + b`
- `a + e * c`
You need to use [[Operator-Precedence Parsing]]
# Process
1. Create a table of precedences
2. Operator-precendece breaks the expression into a stream of primary expressions seperated by binary operators.
3. The expression is a primary expression followed by a sequence of `[binop, primaryexpr]` pairs
