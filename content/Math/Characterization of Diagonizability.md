---
tags:
  - math
  - linalg
---
# Theorem
$T : V \to V$ [[Diagonalizable]] $\Longleftrightarrow$ if $[T]_{\alpha}^{\alpha}$ is similar to the diagonal matrix
# Proof
### Proving $\implies$
- If $T$ is diagonizable, we have a basis $a = \{ v_{1},\dots,v_{n} \}$ such that $T(v_{i}) = \lambda_{i}v_{i}$ for eigenvalues $\lambda_{i}$
- If we have $[T]_{\alpha}^{\alpha}$ in this basis, we get:
$$
[T]_{\alpha}^{\alpha} = \left[\begin{array}{cc}
\lambda_{1} \dots 0\\
0 \dots\lambda_{n} \\
\end{array}\right]
$$
- $= IDI^{-1}$. Therefore, $[T]_{\alpha}^{\alpha}$ is similar to a diagonal matrix
### Proving $\Longleftarrow$