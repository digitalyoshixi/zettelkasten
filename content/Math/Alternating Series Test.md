---
tags:
  - math
  - calculus
aliases:
  - Liebniz Series Test
  - AST
---
# Theorem
- Given $\sum_{n=i}^{\infty}(-1)^{n+1}b_{n}$
- With $b_{n} > 0$
- If $b_{n} \geq b_{n+1}$ $\forall n \in \mathbb{N}$, (just decreasing, not necessarily [[Strictly Decreasing]])
- If $\lim_{ n \to \infty }b_{n} = 0$
- Then, $\sum_{n=i}^{\infty}(-1)^{n+1}b_{n}$ converges
# Proof
1. Given $\sum_{n=i}^{\infty}(-1)^{n+1}b_{n}$, $b_{n} > 0$
2. Suppose $b_{n} > b_{n+1}, \forall n \in \mathbb{N}$
3. Suppose $\lim_{ n \to \infty }b_{n} = 0$
4. We want to show, $\sum_{n=i}^{\infty}(-1)^{n+1}b_{n}$ converges. We prove by definition
5. Consider odd-index set of $\{ S_{n} \}$. This is a [[Monotonic Sequence]]
	1. Then, by [[Bounded Monotone Convergence Theorem|BMCT]], this set converges
6. Consider even-index set of $\{ S_{n} \}$. This is a [[Monotonic Sequence]]
	1. Then, by [[Bounded Monotone Convergence Theorem|BMCT]], this set converges
7. We find later that $\lim_{ n \to \infty }S_{2n} = \lim_{ n \to \infty }S_{2n+1} = s$, then by definition, set converges
8. $\square$
# Example
Prove $\sum_{n=1}^{\infty} \frac{(-1)^{n}}{\ln(n)}$ converges
- Note $b_{n} = \frac{1}{\ln(n)} > 0$
- Note that $\ln(n) < \ln(n+1)$ as [[Natural Logarithms|ln]] is increasing
- $\implies \frac{1}{\ln(n)} > \frac{1}{\ln(n+1)}$
- Thus, $b_{n}$ is decreasing
- Consider $\lim_{ n \to \infty }b_{n} = 0$
- Then, by AST, $\sum_{n=1}^{\infty} \frac{(-1)^{n}}{\ln(n)}$ converges