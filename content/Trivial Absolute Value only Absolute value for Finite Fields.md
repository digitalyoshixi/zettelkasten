---
tags:
  - math
  - linalg
---
# Theorem

# Proof
- Let $y \in \mathbb{F}$ be nonzero
  As $\mathbb{F}$ is a finite field, the set $\{  y, y^{2}, \dots \}$ is finite it follows there exists $0 < a < b < \infty$ such that $y^{a} = y^{b}$ and so, there exists a $0 < k < \infty$ s.t $y^{k} = 1$
- Because $| \cdot |$ is a [[Norm Function]],
- $|y^{k}| = |y^{k}| = |1| = 1$
- So, 
$$
| \cdot | = \begin{cases} 
          \pm 1 & x \text{ is even} \\
          0 & x > 0
       \end{cases}
$$
- So, $| \cdot |$ is an absolute value, it is non-negative, thus $|y| = 1$, it follows that $| \cdot |$ is the trivial absolute value