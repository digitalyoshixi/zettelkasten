---
tags:
  - math
  - linalg
---
# Theorem
A scalar $\lambda$ is an eigenvalue of $T$ $\Longleftrightarrow$ if it is a root of [[Characteristic Polynomial]] $X_{T}$ 
# Proof
### Proving $\implies$
- Suppose $\lambda$ is a [[Eigenvector|Eigenvalue]].
- Then, $T(v) = \lambda v \implies (T-\lambda I)(v) = \overrightarrow{0}$
- Thus, $v \in ker(T - \lambda I)$
- It follows that $T - \lambda I$ is non-invertible by [[Determinants and Invertiblity Theorem]]
- Since, $\det(T - \lambda I) = 0$ it follows $X_{T}(\lambda) = 0$
### Proving $\Longleftarrow$
- Suppose $X_{T}(\lambda) = 0$
- Then, we get $\det(T - \lambda I) = 0$
- Therefore, $ker(T - \lambda I) \neq \{ 0 \}$
- Thus, there is $v \neq 0$ in $ker(T - \lambda I)$
- This gives:
	- $(T - \lambda I)(v) = 0$
	- $\Longleftrightarrow T(v) = \lambda v$
	- Thus, there is some $\lambda$  eigenvector $v$
	- With $\lambda$ as eigenvalue of $T$

