---
tags:
  - calculus
---
# Theorem
given a [[P-Series]]
- If $p \leq 1$, then $\sum_{n=1}^{\infty} \frac{1}{n^{p}}$ diverges
- If $p > 1$, then $\sum_{n=1}^{\infty} \frac{1}{n^{p}}$ converges
# Proof
1. Let $p \in \mathbb{R}^{+}$
2. Given $\sum_{n=1}^{\infty} \frac{1}{n^{p}}$
3. For $\forall n \in \mathbb{N}$, Let $a_{n} = n^{-p} = f(n)$
4. Then, so $f(x) = x^{-p}$ on $[1,\infty)$
5. Note that $x > 0, 1 > 0 \implies \frac{1}{x^{p}} > 0$
6. Note that $\frac{1}{x^{p}}$ is continuous by [[Continuity Theorem]]
7. Note that $\frac{1}{x^{p}}$ is decreasing when $p > 1$ as $\frac{d}{dx} \frac{1}{x^{p}} = -p \frac{1}{x^{p-1}}$. When $p \leq 1$, the derivative is negative
8. Then, by [[Integral Test]] $f$ [[Series Convergence|Converges]]