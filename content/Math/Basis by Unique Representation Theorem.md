---
tags:
  - math
  - linalg
---
$S$ is a basis of $V$ $\Longleftrightarrow$ $\forall \overrightarrow{v} \in V,$ $\overrightarrow{v}$  has a [[Unique Existence|Unique Representation]] in $span(S)$.

# Proof
This proof relies heavily on linear independent sets
### Proving $\implies$
1. Assume $S$ is a basis of $V$
2. Pick $\overrightarrow{v} \in V$, we know $span(S) = V$
3. Then, $\overrightarrow{v} = a_{1} \overrightarrow{v}_{1} + a_{2} \overrightarrow{v}_{2} +\dots a_{n} \overrightarrow{v}_{n} \in span(S)$ Where $a_{i} \in F$, $v_{i} \in S$
4. The vectors in $S$ are lin indep, and so this representation is unique

### Proving $\Longleftarrow$
1. Assume every vector in $V$ has a unique representation in $span(S)$
2. Then, $V \subset span(S)$
3. Therefore, $V = span(S)$. It follows that $S$ is a spanning set of $V$
4. We get that S is [[Linear Independence|Linearly Independent]] because this representation is unique
Therefore, $S$ is a basis.

