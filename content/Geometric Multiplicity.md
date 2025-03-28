---
tags:
  - math
  - linalg
---
# Definition
$Geo(\lambda)$ of an [[Eigenvector|Eigenvalue]] $\lambda$ is the dimension $dim(E_{\lambda})$ for [[Eigenspace]] of $\lambda$
# Example
For the matrix
$$
\left[\begin{array}{cccc} 
1 & 1 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 2 & 0\\
0 & 0 & 0 & 3\\
\end{array}\right]
$$
We get that the [[Eigenvector|Eigenvalues]] are:
$\lambda_{1}=1,\lambda_{2}=2,\lambda_{3}=3$
Finding $Geo(1)$:
- $E_{1} = ker(T - 1I)$
$$
\left[\begin{array}{cccc|c}
0 & 1 & 0 & 0 & 0\\
0 & 0 & 0 & 0& 0\\
0 & 0 & 1 & 0& 0\\
0 & 0 & 0 & 2& 0\\
\end{array}\right]
\xrightarrow{EF}
\left[\begin{array}{cccc|c}
0 & 1 & 0 & 0 & 0\\
0 & 0 & 1 & 0& 0\\
0 & 0 & 0 & 1& 0\\
0 & 0 & 0 & 0& 0\\
\end{array}\right]
$$
Then, $Geo(1) = dim(E_{1}) = 1$