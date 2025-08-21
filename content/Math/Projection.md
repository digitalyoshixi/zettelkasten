---
tags:
  - math
  - linalg
aliases:
  - Projection Operator
---
A linear map that will always map to $\{ 0,1 \}$
# Definition
A projection on $V$ is an operator $E \in \mathcal{L}(V)$ such that $E^{2} = E$
A matrix $A$ is a projection if $A^{2} = A$
# Properties
- With $R = range(E)$
- With $N = ker(E)$
Then,
1. $\beta \in R \Longleftrightarrow \beta = E(\beta)$ (The vector is within the range, if and only if the projection of the vector is equal to itself)
2. $\forall \alpha \in V, E(\alpha) \in R \wedge (I - E)\alpha = N$
3. $E$ is [[Diagonalizable]]
4. $V = R \oplus N$, $\forall v \in V, v = E(v) + (I-E)(v)$
5. Nice matrix representation. $\beta_{R}$ as a basis for $R$, $\beta_{N}$ as a basis for $N$, then $$[E]_{ \{\beta_{R},  \beta_{N}} \}= \left[\begin{array}{cc}
I & 0\\
0 & 0\\
\end{array}\right]$$
# Concepts
- [[Finding a Projection Along a Subspace]]