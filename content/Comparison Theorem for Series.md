---
tags:
  - math
  - calculus
aliases:
  - Direct Comparison Theorem for Series
  - CT
---
# Theorem
### Divergent Case
1. Given $\sum_{n=1}^ {\infty}a_n$, $\sum_{n=1}^{\infty}c_n$, 
2. If $\forall n \in \mathbb{N}$, $0 \leq c_{n} \leq a_{n}$ 
3. And $\sum_{n=1}^{\infty}c_{n}$ [[Series Divergence|Diverges]]
Then, $\sum_{n=1}^{\infty} a_{n}$ also diverges
### Convergent Case
1. Given $\sum_{n=1}^ {\infty}a_n$, $\sum_{n=1}^{\infty}b_n$, 
2. If $\forall n \in \mathbb{N}$, $0 \leq a_{n} \leq b_{n}$ 
3. If $\sum_{n=1}^{\infty}b_n$ [[Series Convergence|Converges]]
Then, $\sum_{n=1}^{\infty} a_{n}$ also converges
# Proof
### Proof for Convergent Case
1. Suppose $\sum_{n=1}^ {\infty}a_n$, $\sum_{n=1}^{\infty}b_n$, exists
2. Suppose $0 < a_{n} < b_{n}$
3. Let $n \in \mathbb{N}$ be arbitrary
4. Consider $S_{n+1} = S_{n} + a_{n+1}$ by defn of [[Series Partial Sum]]
5. Note that $S_{n} \geq 0, a_{n+1} \geq 0$
6. Thus, $S_{n+1} > S_{n}$, which means $\{ S_{n} \}$ is increasing
7. Since, $\forall n \in \mathbb{N}, a_{n} \leq b_{n}$
8. $\implies \sum_{n=1}^{\infty}a_{n} \leq \sum_{n=1}^{\infty}b_{n}$
9. But, since $S_{n} \leq \sum_{n=1}^{\infty}a_{n}$ as $n \in \mathbb{N} \implies n< \infty$ by defn of infinite, as $\{ S_{n} \}$ is increasing
10. So, $S_{n} \leq \sum_{n=1}^{\infty}b_{n} \in \mathbb{R}$ as $\sum_{n=1}^{\infty}b_n$ converges
11. By [[Bounded Monotone Convergence Theorem|BMCT]], $\{ S_{n} \}$ converges
12. Therefore, $\sum_{n=1}^{\infty}a_{n}$ converges by definition
# Example
Find if $\sum_{n=1}^{\infty} \frac{\arctan(n)}{n^{0.5} + 4^{n}}$ converges or diverges
### Soln
Proof
1. For $n \in \mathbb{N}$
2. $a_{n} = \frac{\arctan(n)}{n^{0.5} + 4^{n}} > 0$
3. Note that $4^{n}$ is increasing at a fastest rate
4. Note that $\arctan(n) < \frac{\pi}{2}$
5. Then, $a_{n} < \frac{\pi}{2}\left(  \frac{1}{n^{0.5} + 4^{n}} \right)$
6. $< \frac{\pi}{2}\left(  \frac{1}{4^{n}} \right)$
7. By [[Geometric Series Convergence|GS Test]], our series does indeed convger 