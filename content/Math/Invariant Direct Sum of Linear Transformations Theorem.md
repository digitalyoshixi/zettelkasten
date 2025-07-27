---
tags:
  - math
  - linalg
---
# Theorem
1. Let $T \in \mathcal{L}(V)$
2. Suppose $V = W_{1} \oplus \dots \oplus W_{k}$
3. Let $E_{1} , \dots, E_{k}$ be [[Projection|Projections]] with $range(E_{j}) = W_{j}$
4. Then each $W_{j}$ is invariant for $T \Longleftrightarrow TE_{j} = E_{j}T, \forall 1 \leq j \leq k$
# Proof
1. Suppose $T$ commutes with each $E_{i}$
2. Then, by [[Block Diagonal Basis for Direct Sum of Linear Transformations]] theorem, as $W_{i} = range(E_{i}), W_{i}$ is $T$ [[Invariant]]
3. Suppose $W_{i}$ is $T$ [[Invariant]] for all $i$. Since $E_{i}\alpha \in W_{i}$ and $W$ is invariant under $T$
4. Then, $TE_{i} \alpha = P_{i} \in W_{i}$
5. Now, consider $E_{i}T\alpha$. By construction, $\alpha = E_{1} \alpha + \dots + E_{k} \alpha$
6. Then, $T\alpha = TE_{1}\alpha + \dots + TE_{k}\alpha$
7. As $T E_{j} \alpha = \beta_{j} \in W_{j}, \forall j$
8. Then, 
$$
E_{i}TE_{j} \alpha = = \begin{cases} 
          \beta_{j} & i = j \\
          0 & i \neq j
       \end{cases}
$$
9. $E_{i}T\alpha = E_{i}(T E_{i} \alpha) + \dots + E_{i}(E_{k}\alpha) = 0 + \dots + \beta_{j} + \dots + 0$
# Intuition
We are $T$ invariant $\Longleftrightarrow$ there is a series of projections in the whole space that commute