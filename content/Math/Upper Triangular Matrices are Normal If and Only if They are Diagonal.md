---
tags:
  - math
  - linalg
---
# Theorem
- With $V$ as a finite dimensional inner product space
- With $T \in \mathcal{L}(V)$
- With $\beta$ as an [[Orthogonal Set|Orthogonal Basis]] for $V$
- Suppose that matrix $A = [T]_{\beta}$ is [[Upper Triangular Matrices|Upper Triangular]]
- Then, $T$ is normal $\Longleftrightarrow$ $T$ is a [[Diagonal Matrices|Diagonal Matrix]]
# Proof
1. Since $\beta$ is an [[Orthonormal Set|Orthonormal Basis]], $A^{*} = [T^{*}]_{\beta}$
2. If $A$ is diagonal, then $A A^{*} = A^{*} A$, then this implies: $[T T^{*}]_{\beta} = [T^{*}T]_{\beta}$ which implies $T T^{*} = T^{*}T$
3. Conversely, suppose $T$ is [[Normal Operator|Normal]], and $[T]_{\beta}$ is [[Upper Triangular Matrices|Upper Triangular]]
4. Then, if $\beta = \{  \alpha_{1}, \dots, \alpha_{n} \}$
	1. $T_{\alpha_{1}} = a_{11}\alpha_{1} + 0 \alpha_{2} + \dots + 0 \alpha_{n}$
	2. By our previous theorem, we can say that $T^{*}_{\alpha_{1}} = \overline a_{11} \alpha_{1} + 0 \alpha_{2} + \dots + 0 \alpha_{n}$ as $T_{\alpha_{1}}$ is an [[Eigenvector]] with eigenvalue. 
	3. This implies that $a_{1i} = 0, \forall i \geq 2$
	4. We continue with [[Induction]], to show that $\alpha_{jj+1} = 0, \forall i \in \{ i,\dots, n-j\}$
5. Thus, $A$ is [[Diagonal Matrices|Diagonal]]