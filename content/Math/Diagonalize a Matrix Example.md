---
tags:
  - math
  - linalg
aliases:
  - Finding Diagonals From Eigenvalues
---
# Process
1. Find eigenvalues
2. Find eigenvectors
3. Perform change of basis with the new set of eigenvectors. Note that this set is linearly independent.
# Example
Diagonalize
$$
\left[\begin{array}{cc}
0 & 3 & 0\\
1 & 0 & -1\\
0 & 2 & 0\\
\end{array}\right]
$$
- Find eigenvalues and eigenvectors
$$
X = \det
\left[\begin{array}{cc}
-\lambda & 3 & 0\\
1 & -\lambda & -1\\
0 & 2 & -\lambda\\
\end{array}\right]
= -\lambda^{3} + \lambda
= \lambda(1-\lambda)(1+\lambda)
$$
- We get eigenvalues $0,1,-1$
	- For 0-eigenvector, we find a non-zero solution for $(M - 0(I))x = 0$
		- Then, we get:
$$
\left[\begin{array}{ccc|c}
1 & 0 & -1 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 0\\
\end{array}\right]
$$
		- We can pick a $(1,0,1)$ as an eigenvector
	- For $1$-eigenvector, we find a non-zero soln for $(M - 1I)x = 0$
		- Then, we get:
$$
\left[\begin{array}{ccc|c}
1 & 0 & -\frac{3}{2} & 0\\
0 & 1 & -\frac{1}{2} & 0\\
0 & 0 & 0 & 0\\
\end{array}\right]
$$
		- We can pick a $(3,1,2)$ as an eigenvector
	- For $(-1)$-eigenvector, we find a non-zero soln for $(M + 1I)x = 0$
		- We can pick a $(3,-1,2)$ as an eigenvector
- Hence, we have eigenvector-value pairs $(0)(1,0,1) , (1)(3,1,2), (-1)(3,-1,2)$
- Now, we perform change of basis. with new basis $\{ (1,0,1), (3,1,2), (3,-1,2) \}$
- 
$$
[T]_{\alpha}^{\alpha} = 
\left[\begin{array}{cc}
0 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & -1\\
\end{array}\right]
$$