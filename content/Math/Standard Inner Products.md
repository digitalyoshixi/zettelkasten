---
tags:
  - linalg
  - math
---
# Inner Product
Standard inner product of vector $u,v$ is:
$\langle u,v \rangle = \sum_{k=1}^{n}u_{i}v_{i} = u_{1}v_{1}+\dots+u_{n}v_{n}$
# Length of Norm
The length of the normal $\mid\mid v\mid\mid = \sqrt{ (v,v) } = \sqrt{ v_{1}^{2} + \dots +v_{n}^{2} }$
Note that the inner product is linear in the sense that $\langle u, av = bw \rangle = a \langle u,v \rangle + b \langle u,w \rangle$
# Properties of Standard Inner Product over $\mathbb{R}^{n}$
1. $\langle u,v \rangle = \langle v,u \rangle$
2. $\langle u,v_{1}+v_{2} \rangle = \langle u,v_{1} \rangle + \langle u,v_{2} \rangle$
3. $\langle u,av \rangle = a \langle v,u \rangle$
4. $\langle u,u \rangle \geq 0$ with equality if $u = \overrightarrow{0}$
### Proofs
- [[Proving Standard Inner Function Property 2]]
- [[Proving Standard Inner Function Property 3]]
# Theorems
- [[Inner Products Define Angles Theorem]]
- [[Orthoganality Theorem]]