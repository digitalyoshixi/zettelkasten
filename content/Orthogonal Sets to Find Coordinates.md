---
tags:
  - math
  - linalg
---
# Corrolary
1. If $\{  \alpha_{1} ,\dots, \alpha_{m} \}$ is a [[Orthogonal Set]] of non-zero vectors that spans $V$
2. Then, $\forall \beta \in V, \beta = \sum_{i=1}^{m} \frac{\langle \beta | \alpha_{k} \rangle}{|| \alpha_{k} || ^{2}} \alpha_{k}$

This allows you to find a coordinate by just using the inner product with one orthogonal vector.
This ties into how nice matrixes are formed.
# Example
- Find the coordinate form of $(1,3)$ using the orthogonal basis $\beta = \{ \frac{1}{\sqrt{ 2 }} (1,1) , \frac{\sqrt{ 1 }}{2}(1,-1)\}$
$$
[(1,3)] = [\begin{array}{cc} 
\langle (1,3) | (\frac{1}{\sqrt{ 2 }}, \frac{1}{\sqrt{  2 }}) \\
\langle (1,3) | (\frac{1}{\sqrt{ 2 }} , - \frac{1}{\sqrt{  2 }})\\
\end{array}]$$
$$[(1,3)] = (\frac{4}{\sqrt{  2 }}, -\frac{2}{\sqrt{  2 }})$$