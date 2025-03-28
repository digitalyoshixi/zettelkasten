---
tags:
  - math
  - proofs
---
# Theorem
- Suppose $V$ is a $n$ dimensional $\mathbb{R}$ vector space
- If $T : V\to V$ has a real eigenvalue $\lambda$
- Then, $Geo(\lambda) \leq Alg(\lambda)$
# Proof
### Intuition
Pick a basis of $E_{\lambda}$ then extend it to a basis $\alpha$ of $V$, and compute $X(\lambda)$ in that basis
### Proof
1. We have $dim(E_{\lambda}) = Geo(\lambda) = k$
2. We pick basis $E_{\lambda} = span \{ v_{1} ,\dots,v_{k} \}$
3. We extend this to basis of $V$
4. $v = span(\alpha) = \{ v_{1}  ,\dots, v_{k} , v_{k+1} , \dots, v_{n}\}$
5. In this basis: $T(v_{1}) = \lambda v_{1} , \dots, T(v_{k}) = \lambda v_{k}$ meaning everything in our $v$ from $v_{1}$ to $v_{k}$ is a eigenvector
6. We also know that $v_{k+1}$ to $v_{n}$ are no longer [[Eigenvector|Eigenvectors]]. $T(v_{k+1}) = a_{11}v_{1} + \dots + a_{1n}v_{n}, \dots, T(v_{n}) = a_{n1}v_{1} + \dots + a_{nn}v_{n}$
7. In this basis, we get:
$$
[T]_{\alpha}^{\alpha} = 
\left[\begin{array}{ccc|ccc}
\lambda & \dots  & 0 & a_{11} & \dots & a_{1n}\\
\vdots\\
0 & \dots  & \lambda & a_{n1} & \dots & a_{nn}\\
\end{array}\right]
$$
8. Expanding $X(l) = \det([T]_{\alpha}^{\alpha} - l I) = (\lambda - l)^{k} \det(\text{smaller (n-k) * (n-k) matrix})$
9. This will contain more $l$ terms. We might get more factors $\lambda - l$ or we might not
10. This gives $Alg(\lambda) \geq Geo(\lambda)$