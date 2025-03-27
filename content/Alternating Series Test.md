---
tags:
  - math
  - calculus
aliases:
  - Liebniz Series Test
---
# Theorem
- Given $\sum_{n=i}^{\infty}(-1)^{n+1}b_{n}$
- With $b_{n} > 0$
- If $b_{n} \geq b_{n+1}$ $\forall n \in \mathbb{N}$, (just decreasing, not [[Strictly Decreasing]])
- If $\lim_{ n \to \infty }b_{n} = 0$
- Then, $\sum_{n=i}^{\infty}(-1)^{n+1}b_{n}$ converges
# Example
Prove $\sum_{n=1}^{\infty} \frac{(-1)^{n}}{\ln(n)}$ converges
- Note $b_{n} = \frac{1}{\ln(n)} > 0$
- Note that $\ln(n) < \ln(n+1)$ as [[Natural Logarithms|ln]] is increasing
- $\implies \frac{1}{\ln(n)} > \frac{1}{\ln(n+1)}$
- Thus, $b_{n}$ is decreasing
- Consider $\lim_{ n \to \infty }b_{n} = 0$
- Then, by AST, $\sum_{n=1}^{\infty} \frac{(-1)^{n}}{\ln(n)}$ converges