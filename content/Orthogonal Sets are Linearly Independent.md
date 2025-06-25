---
tags:
  - math
  - linalg
---
# Theorem
1. Let $V$ be an [[Inner Product Space]]
2. An [[Orthogonal Set]] $S \subset V$ of non-zero vectors is linearly independent
# Proof
1. With $\alpha_{1},\dots,\alpha_{n}$ be distinct non-zero vectors
2. In $S$, Let $\beta = c_{1}\alpha_{1} +\dots + c_{n}\alpha_{n}$
3. Then, $\langle \beta | \alpha_{k} \rangle$
4. $= \langle \sum_{i=1}^{n} c_{i}\alpha_{i} | \alpha_{k} \rangle$
5. $= \sum_{i=1}^{n} \langle \alpha_{i} | \alpha_{k}\rangle$
6. $= \sum_{i=1}^{k}c_{i} * 0 + c_{k} \langle \alpha_{k}| \alpha_{k} \rangle + \sum_{i=k+1}^{n}c_{i} * 0$
7. $= c_{k} * || \alpha_{k} ||$
8. Thus, $c_{k} = \frac{\left\langle  \beta | \alpha_{k} \right\rangle}{|| \alpha_{k}|| ^{2}}, \forall 1 \leq k \leq n$
9. This is valid as $\alpha_{k} \neq 0$
10. If $\beta = 0$, then $c_{k} = 0$. Therefore, $( \alpha_{1},\dots,{\alpha_{n}})$ is linearly independent