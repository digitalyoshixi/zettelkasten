---
tags:
  - programming
aliases:
  - CFG to Lattice
  - Transfer Function
  - Join Point
---
Converting a [[Control Flow Graph|CFG]]'s information into a [[Lattice]] to summarize program state.
# Process
For target variable `x`:
- When `x` is declared but not initialized, set this as $\bot$
- When `x` is defined concrete values, it is the set with only that value
- When `x` is defined some unknown value, it can have any value, represent this as $\top$
- When two control flow paths join, the value of `x` is the set union of incoming values ([[Lattice Joining]] + [[Lattice Widening]] to optimize)
- When you get a statement like a transfer function, the set is the value of that statement applied to each element of the set ([[Isomorphism|Isomorphic]] function)
- Continue until you reach a [[Fixed Point]] (values don't change)
![[Control Flow Graph to Lattice-20260621203630116.webp]]
# Statement Transfer Function
![[Control Flow Graph to Lattice-20260621201332066.webp]]
# Control Flow
![[Control Flow Graph to Lattice-20260621203511388.webp]]
