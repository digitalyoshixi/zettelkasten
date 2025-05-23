---
tags:
  - linalg
  - math
---
# Theorem
- With $dim(V) = n$
- $dim(W)= m$
- Then, $n,m < \infty$
- Then, $dim(L(V,W)) =mn$
# Proof
- Let $\beta = \{  \alpha_{1},\dots,\alpha _{n} \}$ be an ordered basis
- Let $\beta^{'} = \{ \beta_{1},\dots,\beta_{m} \}$ be an ordered basis
- For $V,W$, for each pair $(p,q)$ with $1 \leq p \leq m, 1 \leq q \leq n$
- Define a map $E_{pq} \in L(V,W)$ with :
$$
E_{pq}(a_{i}) = \begin{cases} 
 B_{p}, i = q \\
0, i \neq q       \end{cases}
       = \delta_{ip}\beta_{p}, 
\delta_{ip} = \begin{cases} 
 1, i = q \\
0, i \neq q       \end{cases}
$$
We can show that if $T \in L(V,W)$, then $T = \sum_{n}^{i=1} \sum_{m}^{j=1}E_{ij}$ and $\{  E_{ij} | 1 \leq i \leq m, 1 \leq j \leq m\}$ is [[Linear Independence|Linearly Independent]]
