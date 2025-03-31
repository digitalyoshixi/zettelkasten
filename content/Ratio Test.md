---
tags:
  - math
  - calculus
aliases:
  - RT
---
# Theorem
1. Let $\sum a_{n}$ where $\forall n \in \mathbb{N}, a_n \neq 0$
2. Defining $\lim_{ n \to \infty }| \frac{a_{n+1}}{a_{n}}| = L \in \mathbb{R}$
3. If $L < 1$, then $\sum a_{n}$ [[Absolute Convergence]]
4. If $L > 1$ then, $\sum a_{n}$ [[Series Divergence|Diverges]]
5. If $L = 1$ then, this test is inconclusive. Go use another [[Convergence Tests|Convergence Test]]

Often good when used with:
- [[Factorials|Factorial]]
- [[Euler's Number|Exponential Function]]
# Example
Prove $\sum_{n=1}^{\infty} \frac{e^{n}}{(2n)!}$ [[Series Convergence|Converges]].
### Proof
1. We can use R.T
2. Consider $\lim_{ n \to \infty }| \frac{a_{n+1}}{a_{n}}|$
3. $= \lim_{ n \to \infty } | \frac{\frac{e^{n+1}}{(2n+2)!}}{ \frac{e^{n}}{(2n)!}}|$
4. $= \lim_{ n \to \infty }| \frac{e}{(2n+1)(2n+2)}| = 0$
5. Then, as $0 < 1$, this means $\sum a_{n}$ converges