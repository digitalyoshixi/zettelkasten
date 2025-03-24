---
tags:
  - calculus
  - math
aliases:
  - Direct Comparison Theorem for Integrals
  - CT
---
A theorem to easier determine if a [[Improper Integral]] converges or diverges.
# Theorem
1. Suppose $f,g,h$ are continuous on interval $[a,b]$
2. Consider $\int_{a}^{b}f(x)dx$ is an improper integral
3. Convergent case:
	1. If $\forall x \in [a,b],0\leq f(x) \leq g(x)$
	2. And, we also know that $\int_{a}^{b}g(x)dx$ converges
	3. Then, $\int_{a}^{b}f(x)dx$ also converges
4. Divergent case:
	1. If $\forall x \in [a,b], 0 \leq h(x) \leq f(x)$
	2. And, we know that $\int_{a}^{b}h(x)dx$ diverges
	3. Then, $\int_{a}^{b}f(x)dx$ also diverges
# Proofs
- [[Comparison Theorem Convergent Case Proof]]
# Examples
### Example 1
Consider $\int_{0}^{\infty}e^{-x^{2}}dx$. Determine if it converges or diverges
1. Note that $g(x) = e^{-x}$ converges to 0 as $\lim_{ n \to \infty }e^{-n} = 0$
2. By union interval property $\int_{0}^{\infty}e^{-x^{2}}dx = \int_{0}^{1}e^{-x^{2}}dx + \int_{1}^{\infty}e^{-x^{2}}dx$
3. Note that on $x \in [1,\infty)$, $0 \leq e^{-x^{2}} \leq e^{-x}$ as $x > 1 \implies x^{2} \geq x$ as $e^{x}$ is increasing
4. Then, consider $\int_{0}^{\infty}e^{-x}dx$
5. $= \lim_{ A } \to \infty \int_{A}^{0}e^{-x}dx = \lim_{ A \to \infty } -e^{-A} + e^{-1} = \frac{1}{e}$
6. This implies that $\int_{I} f(x)dx$ converges by [[Comparison Theorem for Interals]]