---
tags:
  - linalg
---
# Theorem
1. Suppose $V$ has a finite spanning set $T = \{ y_1, \dots, y_n\}$
2. Suppose $S = \{x_1, \dots, x_k\}$ is a linearly independent subset of $V$
3. There is always a finite basis $S'$ of $V$ such that $S \subset S'$
The idea is set $S' = S$
# Proof 
### Process
1. If $S'$ is a basis, then we're done. Otherwise, union a vector of $T$ with the set of $S$ to create a new linear independent set $S' = S  \cup \{ \vec{y}_i\}$/ (Read [[Linear Independence]])
2. Repeat until $S'$ is a basis
### Proof
1. Assume $S' = S$ is not a basis
2. We know $S'$ is [[Linear Independence]] therefore, $span(S') = V$
3. We find, $y_i \in T$ s.t $\vec{y}_i \not\in S'$ (This is because if all of the guys in $S$ are in $T$, then $span(S) = V$ because $T$ is a spanning set)
4. It follows by the extension of [[Linear Independence Extension Lemma]] that $S' \cup \{ \vec{y}_2 \}$ is linearly independent
5. Run the algorithm again. Now consider $S' \cup \{ \vec{y}_2\} = S$
6. The finiteness of T means that we run this algorithm finitely many times. Therefore, the final $S$ has at most $k+n$ elements which is finite.