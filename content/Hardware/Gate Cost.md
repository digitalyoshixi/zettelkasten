---
tags:
  - hardware
aliases:
  - Gate Input Cost
  - GIC
---
# Gate Cost
The gate cost is the summation of the inputs to a gate.
It is derived from the sum of:
- [[Boolean Literal|Boolean Literals]]
- [[Boolean Term]] gates
# Example
![[Gate Cost-20250806143813080.webp]]
- There are 3 [[Boolean Literal|Literals]] ($A$, $B$, $C$)
- There are three boolean terms ($\overline C \overline A$, $\overline A B$, $\overline B \overline C$)
$$G(Y)= 3+2+2+2=9$$
