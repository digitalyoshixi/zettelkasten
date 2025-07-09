---
tags:
  - math
  - linalg
---
# Theorem
- Let $V$ be a finite-dimensional [[Complex Inner Product Space]].
- Let $T$ be a [[Linear Operator]] on $V$
- Then, there is a [[Orthonormal Set|Orthonormal Basis]] for $V$ in which the matrix of $T$ is [[Upper Triangular Matrices|Upper Triangular]]
# Intuition
- If i show a matrix is normal, then I know it is [[Diagonalizable]], and I know the eigenvectors are perpendicular to eachother
# Proof
We show this with [[Induction|PMI]].
### Base Case
When $dim(V) = 1, [T]_{\alpha} = [\alpha_{u}]$ which is [[Upper Triangular Matrices|Upper Triangular]].
### N+1 Case
- With $dim(V) = n+1$
- Assume that if $W$ is a complex inner product space of dimension $n$, then there exists a [[Orthonormal Set|Orthonormal Basis]] such that the matrix of $T$ is [[Upper Triangular Matrices|Upper Triangular]]
- Recall that since $V$ is a fin-dim inner product space, there exists an eigenvalue, eigenvector pair such that $T \alpha = c \alpha$
- Let $W = span \{ \frac{\alpha}{|| \alpha ||}\}$. Let $W^{ \perp} = span \{  v_{1} ,\dots, v_{n} \}$
- Let $\beta = \{ \frac{\alpha}{|| \alpha ||} , v_{1} ,\dots, v_{n}\}$
- Then, $$[T]_{\beta} = \left[\begin{array}{cc} 
1 & V\\
0 & W\\
\end{array}\right]$$
- Then, let $S_{W} : W^{\perp} \to W^{\perp}$ be defined using the matrix $W$
- Then, by our inductive hypothesis, this is a [[Linear Transform|Linear Map]] from a $n$ dimension vector space to a $n$ dimensional vector space
- Therefore, there exists a basis $\beta' = \{  \alpha_{1}, \dots, \alpha_{n} \}$ such that $[ S_{W} ]_{\beta}^{\beta'}$ is [[Upper Triangular Matrices|Upper Triangular]]
- Note then that $\{  \frac{\alpha}{|| \alpha ||}, \beta' \} = \{  \frac{\alpha}{|| \alpha ||}, \alpha_{1}  , \dots, \alpha_{n}\}$ is an orthonormal basis for $V$
- Let $P$ be the change of basis matrix at $[S_{W}]_{\beta'} = P W P^{-1}$
- Then, $$\left[\begin{array}{cc} 
1 & 0\\
0 & P\\
\end{array}\right]$$ for $\beta$ to $P'$
