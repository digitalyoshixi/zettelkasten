---
tags:
  - math
  - linalg
---
# [[Linear Algebra Done Right Theorem]]
1. Suppose $V$ is a $n-dim$ real vector space
2. Then. if $T : V\to V$ is a [[Linear Transform|Linear Map]]
3. Then, $\{  I, T^{1} , \dots, T^{n+n}\}$ is linearlly dependent in $L(V,V)$
4. Alternatively, there are non-zero constants such that $Z = a_{n+n}T^{n+n} + \dots + a_{1}T^{1} + a_{0}I$
5. Where $T : V \to V$ is the identity and $Z : V\to V$ is the zero map
# Examples
Find a linear dependence among the powers of 
$$
\left[\begin{array}{cc}
1 & 1\\
1 & 0\\
\end{array}\right]
$$
### Soln
$$
I = \left[\begin{array}{cc}
1 & 0\\
0 & 1\\
\end{array}\right]
$$
$$
T^{1} = \left[\begin{array}{cc}
1 & 1\\
1 & 0\\
\end{array}\right]
$$
$$
T^{2} = \left[\begin{array}{cc}
1 & 1\\
1 & 0\\
\end{array}\right]^{2} = 
\left[\begin{array}{cc}
1 & 1\\
1 & 0\\
\end{array}\right] + 
\left[\begin{array}{cc}
1 & 0\\
0 & 1\\
\end{array}\right] 
$$
This gives $T^{2} = T + I$
Thus, $T^{2} - T - I = Z$
Thus, our set $\{ I, T,\dots,T_{n} \}$ is [[Linear Dependence|dep]]