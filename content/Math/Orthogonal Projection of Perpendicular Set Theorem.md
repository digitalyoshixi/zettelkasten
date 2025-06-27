---
tags:
  - math
  - linalg
---
# Theorem
- With $V$ as an [[Inner Product Space]]
- $W$ is a finite-dimensional [[Subspace]] of $V$
- With $E$ as the [[Orthogonal Projection]] $V$ on $W$
- The mapping $(I - E)(\beta) = \beta - \sum_{i=1}^{n} \langle \beta | \alpha_{i} \rangle \alpha_{i}$ is the orthogonal projection of $V$ on $W^{\perp}$ (The $Range(I -E) = W^{\perp}$)
# Proof
1. Let $\beta$ be an arbitrary vector in $V$
2. Then, it follows from the properties of [[Best Approximation]] that  $\beta - E (\beta) \in W^{\perp}$
3. Additionally, $\forall \gamma \in W^{\perp}$, $\beta - \gamma = E(\beta) + (\beta - E(\beta) - \gamma)$
4. Since $E(\beta) \in W$ and $\beta - E(\beta) - \gamma \in W^{\perp}$
5. From [[Generalized Pythagorean Theorem]], and [[Triangle Inequality]], $|| \beta - \gamma || ^2 = || E(\beta) || ^2 + || \beta - E(\beta) - \gamma || ^2 \geq || \beta - E(\beta)||^{2}$ with strict inequality when $\gamma \neq \beta - E(\beta)$
6. Thus, $P - E(\beta)$ is the [[Best Approximation]] in $W^{\perp}$