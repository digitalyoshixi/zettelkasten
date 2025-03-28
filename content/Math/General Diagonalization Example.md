---
tags:
  - math
  - linalg
---
# Process
1. Find the eigenvalues
2. Find the algebraic multiplicity of each eigenvalue
3. Check if $dim(V) = m_{1} + \dots + m_{k}$
4. Check each $dim(E_{\lambda_{i}}) = m_{i}$
# Example
Determine if
$$
\left[\begin{array}{ccc}
1 & 1 & 0\\
0 & 1 & 2\\
0 & 0 & 3\\
\end{array}\right]
$$
is diagonizable
1. Find eigenvalues
$$
X(\lambda) = 
\det \left[\begin{array}{ccc}
1 - \lambda & 1 & 0\\
0 & 1 - \lambda & 2\\
0 & 0 & 3-\lambda\\
\end{array}\right]
$$
$X(\lambda) = (1-\lambda)^{2}(3-\lambda)$
2. Find [[Algebraic Multiplicity]].
- $Alg(1) = 2$
- $Alg(2) = 1$
3. Then, we have:
$dim(V) = 3 = 2 + 1 = Alg(1) + Alg(3)$ (This is the condition of general diagonizability)
4. Then, we check $Alg(1) = Geo(1)$ and $Alg(3) = Geo(3)$
5. Compute $E_{1} = ker(T - 1I)$
$$
\Longleftrightarrow
\left[\begin{array}{ccc|c} 
1 - 1 & 1 & 0 & 0\\
0 & 1-1 & 2 & 0\\
0 & 0 & 3-1 & 0\\
\end{array}\right]
\xrightarrow{EF}
\left[\begin{array}{ccc|c} 
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 0\\
\end{array}\right]
$$
6. Then, $E_{1} = span\{ (1,0,0) \}$
7. This gives $Geo(1) = dim(E_{1}) = 1$
8. Note that $Geo(1)=  1, Alg(1) = 2$. It fails the condition of general diagonizable