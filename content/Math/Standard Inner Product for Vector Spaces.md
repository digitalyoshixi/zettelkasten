---
tags:
  - math
  - linalg
aliases:
  - Inner Product
---
# Definition
1. With $V$ as a vector space over $\mathbb{F}$
2. $\forall \alpha, \beta, \gamma \in V$, $\forall c \in \mathbb{F}$
3. An inner product $\langle \cdot , \cdot \rangle : V \times V \to \mathbb{F}$ has properties
	1. $\langle \alpha + \beta | \gamma \rangle = \langle \alpha + \beta \rangle + \langle \beta + \gamma \rangle$
	2. $\langle c \alpha | \beta \rangle = c \langle a | \beta \rangle$
	3. $\langle \beta | \alpha \rangle = \overline{\langle \alpha | \beta \rangle}$ ([[Conjugate Symmetry]])
	4. $\langle \alpha | \alpha \rangle > 0$ if $\alpha \neq 0$
# Example
With $\alpha = (x_{1},\dots,x_{n})$
With $\beta = (y_{1},\dots y_{n})$
Over $\mathbb{C} \implies \alpha \cdot \beta = \sum_{j=1}^{n}x_{j} \overline y_{j} = \langle \alpha, \beta \rangle$
### Proof
##### Proving $\langle \alpha + \beta | \gamma \rangle = \langle \alpha | \gamma \rangle + \langle\beta | \gamma \rangle, \forall \alpha, \beta, \gamma \in \mathbb{R}^n$
1. Over $\mathbb{C}$,  $\langle \alpha + \beta | \gamma \rangle = \langle (x_{1},\dots,x_{n}) + (y_{1},\dots,y_{n}) | (z_{1},\dots,z_{n}) \rangle$
2. $= \langle (x_{1}+y_{1},\dots,x_{n}+y_{n} | (z_{1},\dots,z_{n})\rangle$
3. $= \sum_{i=1}^{n}(x_{i} + y_{i}) \overline z_{i}$
4. $= \sum_{i=1}^{n}(x_{i}) \overline z_{i} + \sum_{i=1}^{n} x_{i}\overline z_{i}$
5. $= \langle\alpha, \gamma \rangle + \langle\beta , \gamma \rangle$
... for the other 4 axioms
# Theorems
- [[Basic Properties of Inner Products]]
- [[Inner Products Define a Norm]]
- [[Nice Inner Product]]
- [[Polarization Identity]]
- [[Matrix Representation of Inner Product]]