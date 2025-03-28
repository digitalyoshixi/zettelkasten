---
tags:
  - math
  - linalg
---
# Theorem
- Suppose $V$ is a n-dim $\mathbb{R}$ vector space
- If $T : V\to V$ has $n$ distinct $\mathbb{R}$ eigenvalues, then $T$ is [[Diagonalizable]]
# Proof
1. Suppose $T : V\to V$ has $n$ distinct real eigenvalues
2. For each eigenvalue, $\lambda_{i}$, we can find a non-zero eigenvector $v_{i}$ s.t $T(v_{i}) = \lambda_{i}v_{i}$ by definition of eigenvalue
3. Because eigenvalues are distinct by [[Eigenvectors of Distinct Eigenvalues are Independent]] thoerem, $\{ v_{1},\dots,v_n \}$ is [[Linear Independence|Linearly Independent]]
4. It follows that $\alpha = \{ v_{1}, \dots, v_{n} \}$ is a basis of $V$ because $V$ is $n$ dimensional and $|a| = n$.
5. Then, this basis 
$$
[T]_{\alpha}^{\alpha} = 
\left[\begin{array}{cc}
\lambda_{1} \dots 0\\
0 \dots \lambda_{n}\\
\end{array}\right]
$$
Therefore, $T$ is diagonizable