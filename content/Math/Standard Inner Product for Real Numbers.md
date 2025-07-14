---
tags:
  - math
  - linalg
aliases:
  - Dot Product
---
This is not a operation you can always do.
# Definition
- With $V = \mathbb{R}^{n}$
- Fix $\alpha \in \mathbb{R}^{n}$
- The inner product $\langle \cdot | \cdot \rangle : V \times V \to \mathbb{R}$
- With $x = (x_{1},\dots,x_{n})$
- With $y = (y_{1},\dots,y_{n})$
Then, $\langle x | y \rangle = \sum_{i=1}^{n}x_{i}y_{i}$
Alternatively, $\langle x | y \rangle = x^{T}y$
# Properties of Standard Inner Product over $\mathbb{R}^{n}$
1. $\langle u,v \rangle = \langle v,u \rangle$
2. $\langle u,v_{1}+v_{2} \rangle = \langle u,v_{1} \rangle + \langle u,v_{2} \rangle$
3. $\langle u,av \rangle = a \langle v,u \rangle$
4. $\langle u,u \rangle \geq 0$ with equality if $u = \overrightarrow{0}$
### Proofs
- [[Proving Standard Inner Function Property 2]]
- [[Proving Standard Inner Function Property 3]]