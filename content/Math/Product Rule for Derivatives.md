---
tags:
  - math
  - calculus
---
# Product Rule
- Suppose $f : \mathbb{R}^{n} \to \mathbb{R}^{k}$ is a [[Vector Space]]
- Let $c : \mathbb{R}^{n} \to \mathbb{R}$ be a scalar field
- Suppose both $f$ and $c$ are [[Differentiability|Differentiable]] at $x_{0}$
- Let $h(x) = c(x)f(x) : \mathbb{R}^{n}\to \mathbb{R}^{k}$
- $Dh(x_{0}) = c(x_{0}) D f(x_{0})+f(x_{0}) Dc(x_{0})$
### Intuition
- $D h(x_{0})$ and $Dc(x_{0})Df(x_{0})$ are both $n \times k$ matrix
- $f(x_{0})$ is a $1 \times k$ matrix
- $Dc(x_{0})$ is a $n \times 1$ matrix

$$h(x,y) = xy\left[\begin{array}{cc}
x\\
y
\end{array}\right]$$Where:
- $c(x) =xy$
- $$f(x)= \left[\begin{array}{cc} 
x\\
y
\end{array}\right]$$