---
tags:
  - math
---
A set of [[Tuple]] showing how a set is related.
# Formal Definition
A relation $R$ is a subset of [[Cartesian Product]] of two sets with a relation operation.
$R \subset A \times B$.
- $\{ (a,b) | aRb \}$
# Properties
### [[Reflexive]]
$R$ is reflexive if $\forall a \in A, (a,a) \in R$
### [[Symmetric]]
$R$ is symmetric if $\forall a,b \in A, (a,b) \in R\implies (b,a) \in R$
### [[Transitive]]
$R$ is transitive if $\forall a,b,c \in A, (a,b) \in \mathbb{R} \wedge (b,c) \in R \implies (a,c) \in R$
### [[Antisymmetric]]
R is antisymmetric if $\forall a,b \in A$ s.t $a \neq b, (a,b) \in R \implies (b,a) \not \in R$
### [[Partial Order]]
$R$ is a partial order if it is [[Antisymmetric]] and [[Transitive]]
# Example
$\{ (x,y) |x \text{ loves } y \}$
# Types
- [[Binary Relation]]
- [[Unique Relation]]
- [[Total Relation]]