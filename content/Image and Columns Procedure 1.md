---
tags:
  - malware
  - linalg
---
# Theorem
1. Fix bases $\alpha = \{ v_{1},\dots,v_{n} \}$, $\beta = \{ w_{1},\dots,w_{k} \}$ of $V,W$.
2. Then image $Image(T)$ is spanned by columns of $[T]_{\alpha}^{\beta}$ which contains basic variables of homogeneous system $[T]_{\alpha}^{\beta}[v]_{\alpha} = 0$
# Down to Earth Version
Consider any $p \in P_{3}(\mathbb{R})$
If we take its derivative, we get:
$\frac{d}{dx}[p]$
$= \frac{d}{dx}[a_{0}+a_{1}\mathbf{x}+ a_{2}x^{2}+ a_{3}x^{3}]$
$= 0 + a_{1} + a_{2}*2x + a_{3} * 3x^{2}$
# Example
Where $D$ is the differentiation function, find a basis for the image $D : P_{3}(\mathbb{R}) \to P_{2}(\mathbb{R})$
### Soln
1. Set basis $P_{3}(\mathbb{R}) = span\{ 1,x,x^{2},x^{3} \} = span(\alpha)$
2. Set basis $P_{2}(\mathbb{R}) = span\{ 1,x,x^{2} \} = span(\beta)$
3. Then, the matrix $[D]_{\alpha}^{\beta}$
	1. $D(1) = \frac{d}{dx}[1] = 0*1 + 0*x + 0*x^{2}$
	2. $D(x) = \frac{d}{dx}[x] = 1*1 + 0*x + 0*x^{2}$
	3. $D(x^{2}) = \frac{d}{dx}[x^{2}] = 0*1 + 2*x + 0*x^{2}$
	4. $D(x^{3}) = \frac{d}{dx}[x^{3}] = 0*1 + 0*x + 3*x^{2}$
4. This gives: $$[D]_{\alpha}^{\beta} =
\left[\begin{array}{cccc|c}
0 & 1 & 0 & 0 & 0\\
0 & 0 & 2 & 0 & 0\\
0 & 0 & 0 & 3 & 0\\
\end{array}\right]
$$
5. Find the [[Basic and Free Variables|Basic]] solns of $[D]_{\alpha}^{\beta} [\overrightarrow{v}]_{\alpha} = \overrightarrow{0}$. We get:
	1. $\{ D(x), D(x^{2}), D(x^{3})\} = \{ 1,2x,3x^{2} \}$
