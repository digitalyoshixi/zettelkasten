---
tags:
  - reverse_engineering
  - math
aliases:
  - SMT Solver
---
SMT solvers are magic. They solve CTF challenges like nothing.
They are based off [[Boolean Satisfiability Problem Solvers|SAT Solvers]] but instead of only taking boolean expressions, they can take integers, arrays, arithmetic operations, etc.
# Terminology
### Concrete Values
These are constant integer values like `5`,`1337`,etc.
### Symbolic Values
These are unknown values in expressions.
like `x` and `y` in the expression `3x+2y=1`
### Symbolic Execution
The act of reducing the entirety of your program into mathematical equations and control flow

# Problem with SMT Solvers
- Only feasible for small problems. Complex problems with several inputs will lead to a path explosion where there are too many possible paths for the computer to go down.
