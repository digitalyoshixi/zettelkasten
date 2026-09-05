---
tags:
  - verification
---
The process many [[Active Automata Learning]] follow
Loop:
1. Learner queries [[System Under Learning|SUL]] for its behavior through a [[Membership Oracle]] or [[Equivalence Oracle]]
2. Checks in verification phase whether hypothesis and [[System Under Learning|SUL]] are equivalent ([[Conformance Testing]]), if not then send a counterexample
Continues until model no new states found