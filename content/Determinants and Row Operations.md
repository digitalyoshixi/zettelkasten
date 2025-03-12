---
tags:
  - math
  - linalg
aliases:
  - Matrix Operation Invariance
---
Let $M \in M_{n \times n}(\mathbb{R})$
Suppose $M'$ is obtained from $M$ by row operation
1. Scale a row. if $M \xrightarrow{\lambda R_{i} \to R_{i}} M'$ then $\det(M') = \lambda \det(M)$
2. Exchange a row $R_{i}, R_{j}$ $M \xrightarrow{R_{i} \leftrightarrow R_{j}} M'$ then $\det(M') = -\det(M)$
3. Add a row $R_{i}, R_{j}$ $M \xrightarrow{\lambda R_{i} + R_{j} \to R_{j}} M'$ then $\det(M') = \det(M)$
# Proofs
### Proving Scalability
$\det(M') = \det(R_{1},\dots, \lambda R_{i},\dots,R_{n})$ by multilinearity
$= \lambda \det(R_{1},\dots,R_{i},\dots,R_{n})$
####