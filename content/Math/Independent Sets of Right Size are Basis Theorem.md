---
tags:
  - math
  - linalg
---
Let $V$ be a finite dimensional vector space.
If $S$ is a linearly independent set with $|S|= dim(V)$ then $S$ is a basis for $V$
# Proof
WTS that $S$ is [[Linear Independence|indep]] and $|S| = dim(V)$ $\implies$ $v = span(S)$
Suppose $S$ is [[Linear Independence|indep]] and $|S| = dim(V)$
For sake of contradiction, suppose $V \neq span(S)$
Then, we can extend $S$ to $S' = S \cup{\overrightarrow{v}}$ for $\overrightarrow{v} \not\in span(S)$
This gives a linearly independent set in $V$ of size $|S| + 1 = dim(V) + 1 > dim(V)$
This contradicts the definition of $dim(V)$.
Aka, we get a linearly dependent set that is too big to be in $V$.
therefore, $V = span(S)$