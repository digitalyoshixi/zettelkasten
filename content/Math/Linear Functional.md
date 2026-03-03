---
tags:
  - math
  - linalg
aliases: []
---
Any [[Linear Transform|Linear Map]] that takes in a vector space and outputs a scalar in the same field.
# Formal Definition
- With $V$ as a [[Vector Space]] over [[Math/Field]] $\mathbb{F}$
- [[Linear Transform|Linear Map]] $f \in \mathcal{L}(V,\mathbb{F})$ are called linear functionals
- Linear functional under a vector $\alpha$ are denoted as: $f_{\alpha}(x) = a \cdot x$
# Implementations
- [[Matrix Trace]]
- [[Linear Functional for Real Numbers]]
- [[Linear Functional for Complex Numbers]]
# Example Proof
1. With $V$ as the vector space of [[Math/Polynomial|Polynomials]]
2. Let $t \in \mathbb{F}$
3. Show that $L_{t}(P) = P(t), \forall P \in V$ defines a linear functional $L \in \mathcal{L}(V,\mathbb{F})$
### Soln
1. As $P(t) \in \mathbb{F}, \forall t \in \mathbb{F}$
2. $L_{t}(P) : V \to \mathbb{F}$
3. Let $c \in \mathbb{F}$
4. let $f,g \in V$
5. Then, $L_{t}(cf + g) = (cf+g)(t) = cf(t) + g(t) = cL_{t}(f) + L_{t}(g)$
6. Thus, this is a linear functional