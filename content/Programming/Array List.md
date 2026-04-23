---
tags:
  - programming
aliases:
  - Dynamic Array
  - Expandable Array
---
A general [[Data Structures and Algorithms|Data Structure]] that can grow/shrink in size.
- [[C++ Vectors]]
- [[Java ArrayList]]
# Operations
- `get(i)`: Read `A[i]` for $0 \leq i \leq size(A)$
- `set(i,x)`: Write `A[i] := x` for $0 \leq i \leq size(A)$
- `size()`: Return number of elements in $A$
- `add(x)`: Write $x$ at the end of $A$ if there is space. If $A$ is full, double capacity and copy elements before adding $x$
