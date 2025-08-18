---
tags:
  - math
  - linalg
---
# Theorem
- Let $V$ be a finite-dimensional [[Complex Inner Product Space]].
- Let $T$ be a [[Linear Operator]] on $V$ with matrix $A$
- Then, there is a [[Orthonormal Set|Orthonormal Basis]] such that there is a [[Upper Triangular Matrices|Upper Triangular]] matrix $M$
- Then, there is a [[Unitary Operator|Unitary]] matrix $U$ such that:
$$A = U M U^{*}$$
# Intuition
- If i show a matrix is normal, then I know it is [[Diagonalizable]], and I know the eigenvectors are perpendicular to eachother
This process can be used to find [[Similar Matrixes]] so that further computations are easier
![[Schur's Decomposition-20250718183236899.webp]]
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
- We want to show that we can get to this [[Upper Triangular Matrices|Upper Triangular]] matrix. $$\left[\begin{array}{cc} 
x & VP\\
0 & [S_{w}]_{\beta'}\\
\end{array}\right]$$
- We know that by [[Change of Coordinate]], $[T]_{\beta} = \hat{P}^{-1}[T]_{\beta}\hat{P}$
- $\implies [T]_{\beta'} = \hat{P}[T]_{\beta}\hat{P}^{-1}$
- $$
=\left[\begin{array}{cc} 
1 & 0\\
0 & P\\
\end{array}\right]
\left[\begin{array}{cc} 
C & V\\
0 & W\\
\end{array}\right]
\left[\begin{array}{cc} 
1 & 0\\
0 & P^{-1}\\
\end{array}\right]
$$
- $$
=\left[\begin{array}{cc} 
1 & 0\\
0 & P\\
\end{array}\right]
\left[\begin{array}{cc} 
C \cdot 1 + V \cdot 0 & C \cdot 0 + VP^{-1} \\
0 \cdot 1 + W \cdot 0 & 0 \cdot 0 + WP^{-1}
\end{array}\right]
$$
- Remember that $V$ is a vector, $P$ is a matrix and $W$ is a matrix
- $$
=\left[\begin{array}{cc} 
1 & 0\\
0 & P\\
\end{array}\right]
\left[\begin{array}{cc} 
C \cdot 1 + V \cdot 0 & C \cdot 0 + VP^{-1} \\
0 \cdot 1 + W \cdot 0 & 0 \cdot 0 + WP^{-1}
\end{array}\right]
$$
- $$
=\left[\begin{array}{cc} 
c & VP^{-1}\\
0 & [S_{w}]_{\beta'}\\
\end{array}\right]
$$
- Note that this is [[Upper Triangular Matrices|Upper Triangular]]