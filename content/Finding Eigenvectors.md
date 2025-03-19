---
tags:
  - math
  - linalg
---
This is a tedious process
# Process
1. Find the characteristic polynomial of the matrix
2. Determine the roots of the polynomial, these are your [[Eigenvector|Eigenvalues]] 
3. For each eigenvalue $a$, compute the eigenvector $\overrightarrow{x}$ where $(M - (a)I) \overrightarrow{x} = 0$
# Example
Find all eigenvalues and eigenvectors of 
$$
M = \left[\begin{array}{cc}
1 & 2 \\
4 & 3
\end{array}\right]
$$

1. $X_{M}(\lambda) = \det(M - \lambda I)$
2. $= (1-\lambda)(3-\lambda) - 8$
3. $= (\lambda - 5) (\lambda + 1)$
4. The roots are $\lambda = 5, \lambda = -1$
5. For $\lambda = 5$: we find $(M - (5)I) \overrightarrow{x} = 0$
   $$
\left[\begin{array}{cc|c}
-4 & 2 & 0 \\
4 & -2 & 0 \\
\end{array}\right]
=
\left[\begin{array}{cc|c}
1 & -\frac{1}{2} & 0 \\
0 & 0 & 0 \\
\end{array}\right]

$$
	1. Then, $v = (1,2)$ is a non-zero soln
6. For $\lambda = -1$, we find $(M - (-1)I) \overrightarrow{x}  = 0$
   $$
\left[\begin{array}{cc|c}
2 & 2 & 0 \\
4 & 4 & 0 \\
\end{array}\right]
=
\left[\begin{array}{cc|c}
1 & 1 & 0 \\
0 & 0 & 0 \\
\end{array}\right]
$$
	1. Then, $v = (1,-1)$ is a non-zero soln
7. Thus, we get $(1,2)$ is a $5$-eigenvector
8. Thus, we get $(1,-1)$ is a $(-1)$-eigenvector