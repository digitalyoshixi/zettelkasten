---
tags:
  - linalg
  - math
---
A vector space $V$ over a [[Math/Field]] is a set of vectors that has:
- [[Closed Under Addition]]
- [[Closed Under Scalar Multiplication]]
And both operations follows the 8 axioms:
1. $\boxplus$ is [[Associative]] ($\forall x,y,z \in V, (x+y)+z = x+(y+z)$)
2. $\boxplus$ is [[Commutative]] ($\forall x,y \in V, x+y = y+x$)
3. [[Additive Identity]] ($\exists \overrightarrow{0} \in V$ s.t $\forall x \in V, \overrightarrow{0} + \overrightarrow{x} = \overrightarrow{x}$)
4. [[Additive Inverse]] for all $x$. ($\forall x \in V, \exists x'$ s.t $x+x'=0$)
5. [[Associative]] scalar multiplication $\forall x \in V, \forall c,d \in F, (cd) \overrightarrow{x} = c(d \overrightarrow{x})$
6. [[Distributive]] under addition of vectors ($c \boxdot(\overrightarrow{x} \boxplus \overrightarrow{y})$ = $(c \boxdot \overrightarrow{x}) \boxplus (c \boxdot \overrightarrow{y})$)
7. [[Distributive]] under addition of scalars ($\forall x \in V, \forall c,d \in F, (c+d)(\overrightarrow{x}) = c \overrightarrow{x} + d \overrightarrow{x}$)
8. [[Multiplicative Identity]] $\forall x \in V, 1 \overrightarrow{x} = \overrightarrow{x}$
# Checking Valid Vector Spaces
You need to check that all 8 axioms apply to the vector space.
# Propositions
1. The zero vector $0$ is unique
2. $\forall x \in V, 0x=0$
3. $\forall x \in V, x'$ is unique
4. $\forall x \in V, \forall c \in R, (-c)x = -(cx)$
# Concepts
- [[Subspace]]
- [[Vector Space Dimension]]
- [[Finite Dimension Vector Space Implications]]