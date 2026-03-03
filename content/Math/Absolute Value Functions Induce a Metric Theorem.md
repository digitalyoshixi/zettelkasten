---
tags:
  - math
  - linalg
aliases:
  - All Vector Norms Induce a Metric Theorem
---
# Theorem
[[Norm|Absolute Values]] [[Induce]] a [[Metric]]
- $\mathcal{D}$ as an [[Integral Domain]] or [[Math/Field]]
- Let $| \cdot | : \mathcal{D} \to \mathbb{R}$ be an absolute value
- Let $d(x,y) = |x - y|$
- For all $x,y \in \mathcal{D}$
- Then, $d$ is a metric for $\mathcal{D}$
# Alternate Theorem
- Let $| | \cdot | | : V\to \mathbb{R}$ be a [[Norm]] with $| \cdot |$
- Then, $d ( x, y ) = | | x - y | |$ is a [[Metric]] for $V$
# Proof
### Proving $d(x,y) \geq 0$
- Let $x,y \in \mathcal{D}$, then $d(x,y) = |x-y| \geq 0$ as $| \cdot | \geq 0$
### Proving $d(x,y)  =d(y,x)$
- $d(x,y) = |x-y| = |x + (-y)| - |(-1)(-1)(x) + y|$
- $= |(-1) * (y + (-1)(x)| = |(-1) * (y-x)| = |-1| * |y-x| = |y-x|$ as $|-1| = 1$ 
### Proving $d(x,y) = 0 \Longleftrightarrow x=y$
- $d(x,y) = 0$
- $\Longleftrightarrow |x-y| = 0$ by [[Norm|Absolute Function]] props
- $\Longleftrightarrow x-y = 0$ by defn [[Norm]]
- $\Longleftrightarrow x=y$ by [[Integral Domain]] props
### Proving $d(x,z) \leq d(x,y) + d(y,z)$
- $d(x,z) = |x-z| = |x-y +y-z| = |(x-y) + (y-z)|$
- $\leq |x-y| + |y-z| = d(x,y) + d(y,z)$