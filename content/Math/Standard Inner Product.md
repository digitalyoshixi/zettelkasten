---
tags:
  - linalg
  - math
aliases:
  - Standard Dot Product
---
# Notation
Standard inner product of vector $u,v$ denoted as:
- $\langle u, v \rangle$
- $\langle u| v \rangle$
- $u \cdot v$
Defined differently for the [[Field]]:
- [[Standard Inner Product for Real Numbers]] (Dot product)
- [[Standard Inner Product for Complex Numbers]]
# Definition
1. With $V$ as a vector space over $\mathbb{F}$
2. $\forall \alpha, \beta, \gamma \in V$, $\forall c \in \mathbb{F}$
3. An inner product $\langle \cdot , \cdot \rangle : V \times V \to \mathbb{F}$ has properties
	1. $\langle \alpha + \beta | \gamma \rangle = \langle \alpha + \beta \rangle + \langle \beta + \gamma \rangle$
	2. $\langle c \alpha | \beta \rangle = c \langle a | \beta \rangle$
	3. $\langle \alpha | \alpha \rangle = \overline{\langle \alpha | \beta \rangle}$
	4. $\langle \alpha | \alpha \rangle > 0$ if $\alpha \neq 0$
# Operation
$$\overrightarrow{u}\cdot\overrightarrow{v}=|\overrightarrow{u}|*|\overrightarrow{v}|*\cos\theta$$
$$\overrightarrow{u} \cdot \overrightarrow{v} = u_{1}v_{1}+\dots+u_{n}v_{n}$$
$$(x+y) \cdot w = x \cdot w + y \cdot w$$
# Length of Norm
The length of the normal $\mid\mid v\mid\mid = \sqrt{ (v,v) } = \sqrt{ v_{1}^{2} + \dots +v_{n}^{2} }$
Note that the inner product is linear in the sense that $\langle u, av = bw \rangle = a \langle u,v \rangle + b \langle u,w \rangle$
# Theorems
- [[Inner Products Define Angles Theorem]]
- [[Orthoganality Theorem]]
- [[Standard Inner Product for Complex Numbers]]
- [[Standard Inner Product Function]]
- [[Riesz Representation Theorem]]
- [[Standard Inner Product for Real Numbers]]