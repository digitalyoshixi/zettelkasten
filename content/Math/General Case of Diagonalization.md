---
tags:
  - math
  - linalg
---
# Theorem
1. Suppose $T : V \to V$ is a linear transform of a finite dimensional vector space
2. Suppose $T$ has distinct eigenvalues $\lambda_{1}, \dots, \lambda_{k}$
3. Let $m_{i}$ be the [[Algebraic Multiplicity]] of $\lambda_{i}$
4. Then, $T$ is diagonizable $\Longleftrightarrow$
	1. $dim(V) = m_{1} + \dots + m_{k}$
	2. $dim(E_{\lambda_{i}}) = m_{i}$
# Examples
- [[General Diagonalization Example]]
# Proof
1. Suppose $T : V \to V$ is a linear transform of a finite dimensional vector space
2. Suppose $T$ has distinct eigenvalues $\lambda_{1}, \dots, \lambda_{k}$
3. Let $m_{i}$ be the [[Algebraic Multiplicity]] of $\lambda_{i}$
### Proving $\implies$
1. Suppose $T : V \to V$ is diagonazible
2. In the eigenbasis $\alpha$, we have:
$$
[T]_{\alpha}^{\alpha} = 
\left[\begin{array}{cc}
\lambda_{1} & 0 & \dots & 0\\
0 & \lambda_{1} &  \dots & 0\\
0 &  \dots & 0 & \lambda_{n}\\
\end{array}\right]
$$
3. $Geo(\lambda_{1}) = Alg(\lambda_{1})$
4. If we compare $X(\lambda)$ in this basis, we get $X(\lambda) = (\lambda_{1} - \lambda) Alg(\lambda_{1})$
5. In this matrix, we have $dim(V) = n = Alg(\lambda_{1}) + \dots + Alg(\lambda_{n})$
6. $= m_{1} = \dots + m_{k}$
### Proving $\Longleftarrow$
1. Suppose $T$ satisfies $dim(V) = m_{1}  + \dots + m_{n}= Alg(\lambda_{1}) + \dots + Alg(\lambda_{n})$
2. Then, $Geo(\lambda_{i}) = Alg(\lambda_{i})$ for each $i \in 1,\dots,n$
3. We build an eigenbasis of V with the right size
4. Consider eigenspace $E_{\lambda_{i}}$ for all $i \in 1,\dots ,n$
5. Each of these is a subspace of $V$, so they are all finite dimensional and have basis
6. We have  dim