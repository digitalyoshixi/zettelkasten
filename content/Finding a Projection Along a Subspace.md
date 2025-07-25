---
tags:
  - math
  - linalg
---
# Example
Find a projection $E$ that projects $\mathbb{R}^{3}$ onto $R = span \{ (1,2) \}$ along $N = span \{ 3, -1 \}$
# Solns
### Naive Solns
1. As $\beta = \{  \alpha_{1}, \alpha_{2} \}$ forms a basis for $\mathbb{R}^{n}$
2. Given $\alpha = (x_{1}, x_{2}) \in \mathbb{R}^{2}$, we can solve $a, b \in \mathbb{R}$ (in terms of $x_{1},x_{2}$) such that $a = a \alpha_{1} + b \alpha_{2}$
3. $(x_{1}, x_{2}) = a \alpha_{1} + b \alpha_{2}$
4. For our example, we can solve the system of equations to get: $a = \frac{(x_{1} + 3x_{2})}{7}$, $b = \frac{(2x_{1} + 6x_{2})}{7}$
5. We can then define $E$ by $E(a \alpha_{1} + b \alpha_{2}) = \alpha_{1}$ which explicitly gives $E(x_{1}, x_{2}) = \frac{(x_{1} + 3x_{2})}{7}(1,2) = (\frac{x_{1} + 3x_{2}}{7}, \frac{2x_{1} + 6x_{2}}{7})$
### Matrix Soln
1. As $E(\alpha_{1}) = \alpha_{1}$
2. As $E(\alpha_{2}) = 0$
3. Then, this implies $$[E]_{\beta} = \left[\begin{array}{cc}
1 & 0\\
0 & 0\\
\end{array}\right]$$
Finally, we show that 
$$
[E^{2}]_{\beta} = \left[\begin{array}{cc} 
1 & 0\\
0 & 0\\
\end{array}\right]
\left[\begin{array}{cc} 
1 & 0\\
0 & 0\\
\end{array}\right]
=
\left[\begin{array}{cc} 
1 & 0\\
0 & 0\\
\end{array}\right]
=
[E]_{\beta}
$$
Then, 
$$[E]_{e_{1}, e_{2}} = 
\left[\begin{array}{cc} 
1 & 3 \\ 
2 & -1
\end{array}\right]
\left[\begin{array}{cc} 
1 & 0 \\ 
0 & 0
\end{array}\right]
\left[\begin{array}{cc} 
1 & 3 \\ 
2 &-1 
\end{array}\right]^{-1}
$$
