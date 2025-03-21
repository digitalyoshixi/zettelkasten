---
tags:
  - math
  - linalg
---
An alternative process to [[Finding Eigenvectors]].
# Theorem
- Suppose $T : V\to V$ is a linear map of an $n-dim$ $\mathbb{R}$ vector space.
- Suppose $p(T) = Z$ for some polynomial $p \in P_{n}(\mathbb{R})$
- Then, factors as $Z = T^{n+n} + \dots + a_{1}T^{1} + a_{0}I = (T - \lambda_{k}I)\dots(T-\lambda_{1}I)$
- For any non-zero vector $v \in V$, we have that one of the vectors $(T - \lambda I)v,  (T- \lambda_{2}I)(T - \lambda_{1}I)v, \dots, (T - \lambda_{k-1}I)\dots(T-\lambda_{1}I)v$ is an [[Eigenvector]] of $T$
# Example
Find a dependence of the powers of 
$$
\left[\begin{array}{cc}
1 & 2\\
4 & 3\\
\end{array}\right]
$$
Use this dependence to find eigenvectors and eigenvalues
1. Find a dependence
$$
I = \left[\begin{array}{cc}
1 & 0\\
0 & 1\\
\end{array}\right]
$$

$$
T = \left[\begin{array}{cc}
1 & 2\\
4 & 3\\
\end{array}\right]
$$
$$
T^{2} = \left[\begin{array}{cc}
1 & 2\\
4 & 3\\
\end{array}\right]^{2}
= \left[\begin{array}{cc}
9 & 8\\
16 & 17\\
\end{array}\right]
= 4T + 5I
$$
2. This gives $T^{2} = 4T + 5I \Longleftrightarrow T^{2} - 4T + 5I =Z$
3. We can think of this as $x^{2} - 4x - 5 = 0 \Longleftrightarrow (x-5)(x+1) = 0$
4. So, $(T-5I)(T+I) = Z$
5. We get $\lambda = 5, \lambda = -1$
6. Pick **any** non-zero vector and compute
7. $0 = Z(1,0) = (T - 5I)(T+I) (1,0)$
8. We calculate 
$$(T+I)(1,0) = 
(\left[\begin{array}{cc}
1 & 2\\
4 & 3\\
\end{array}\right] 
+
\left[\begin{array}{cc}
1 & 0\\
0 & 1\\
\end{array}\right] 
)
\left[\begin{array}{c}
1 \\
0 \\
\end{array}\right] 
$$
$$
= \left[\begin{array}{cc} 
2 & 2\\
4 & 4\\
\end{array}\right]
\left[\begin{array}{cc}
1\\
0 \\
\end{array}\right]
=
\left[\begin{array}{cc}
2\\
4 \\
\end{array}\right]
= (2,4)
$$
9. Thus, $(1,0)$ is not a $\lambda=-1$ eigenvector
10. We continue, $(T- 5I)(2,4)$ with the process, putting the last thing as an input
11. 
$$
(\left[\begin{array}{cc}
1 & 2\\
4 & 3\\
\end{array}\right] 
- 5
\left[\begin{array}{cc}
1 & 0\\
0 & 1\\
\end{array}\right] 
)
\left[\begin{array}{c}
2 \\
4 \\
\end{array}\right] 
=

\left[\begin{array}{c}
0\\
0\\
\end{array}\right]
$$
