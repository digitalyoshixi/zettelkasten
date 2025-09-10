---
tags:
  - math
  - programming
  - proofs
---
# Example
- Let $C(n)$ be the data assignments when returning a list of $n$ items using [[Merge Sort]]
- Then,
  $$
 C(n)  = \begin{cases}
 0 & \text{ if n = 1}\\
 2C([\frac{n}{2}]) + 2n & \text{ if n > 1}
\end{cases}
  $$
- Suppose $n$ is a large power of $2$, i.e $n = 2^{k}$ for $k \in \mathbb{N}$
- $C(n) = 2C(\frac{n}{2}) + 2n$               1st iteration
- $= 2( 2C(\frac{n}{4}) + 2(\frac{n}{2})) + 2n$       2nd Iteration
- $= 2^{2}C(\frac{n}{4}) + 4n$
- $= 2^{2}(2C(\frac{n}{2}) + 2( \frac{n}{4})) + 4n$     3rd iteration
- $= 2^{3} C(\frac{n}{8}) + 6n$
- Now we recognize a pattern as:  $2^{i}C (\frac{n}{2^{i}}) + 2in$ as the i-th iteration
- We can generalize to say: 