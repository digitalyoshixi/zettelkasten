---
tags:
  - linalg
---
# Theorem
1. Suppose $V$ is a finite spanning set $T = \{ y_1, \dots, y_n\}$
2. Suppose $S = \{x_1, \dots, x_k\}$ is a linearly independent subset of $V$
3. There is always a finite basis $S'$ of $V$ such that $S \subset S'$
The idea is set $S' = S$
# Proof Process
1. If $S'$ is a basis, then we're don't. Otherwise, union a vector of $T$ with the set of $S$ to create a new linear independent set $S' = S  \cup \{ \vec{y}_i\}$/ (Read [[Linear Independence]])
2. Repeat until $S'$ is a basis