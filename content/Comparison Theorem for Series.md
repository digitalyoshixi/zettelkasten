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
2. If $0 \leq c_{n} \leq a_{n}$ $\forall n \in \mathbb{N}$
3. And $\sum_{n=1}^{\infty}c_{n}$ [[Series Divergence|Diverges]]
Then, $\sum_{n=1}^{\infty} a_{n}$ also diverges
### Convergent Case
1. Given $\sum_{n=1}^ {\infty}a_n$, $\sum_{n=1}^{\infty}b_n$, 
2. Given $0 < a_{n} < b_{n}$
3. If $\sum_{n=1}^{\infty}b_n$ [[Series Convergence|Converges]]
Then, $\sum_{n=1}^{\infty} a_{n}$ also converges
# Proof
### Proof for Convergent Case
1. Suppose $\sum_{n=1}^ {\infty}a_n$, $\sum_{n=1}^{\infty}b_n$, exists
2. Suppose $0 < a_{n} < b_{n}$
3. 
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