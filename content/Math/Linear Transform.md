---
tags:
  - math
aliases:
  - Linear Transformation
  - Linear Map
  - Linear Function
---
A function T that maps vectors from [[Vector Space]] V into another [[Vector Space]] W given by a transformation.
# Definition
- Suppose $(V,\boxplus,\boxdot)$ and $(W,\oplus, \odot)$ are vector spaces.
A linear transformation function of $T : V\to W$ is a function that follows the axioms:
- Additivity $\forall u,v \in V, T(v \boxplus v) = T(u)\oplus T(v)$
- Multiplicative $\forall v \in V, \forall a \in \mathbb{F},  T(a \boxdot v) = a \odot T(v)$
### Implications
This has the further effect of:
- Ensuring all lines are lines (No linear transformation should multiply variables together)
- Ensuring the origin remains at the same position ($T(\overrightarrow{0}) = \overrightarrow{0}$ always)
# Theorems
- [[Linear Transformations Preserve Additive Identities]]
- [[Linear Transformations Preserve Addition and Scaling]]
- [[Linear Maps Determined by Their Actions on A Basis]]
- [[Linear Transformation Characterized by Finite Number of Scalars]]
# Applications
- [[Proving A Function Is Linear]]
# Concepts
- [[Matrix Transformation]]
- [[Zero Transformation]]
- [[Identity Transformation]]
- [[Linear Transformation Rotation]]
- [[Linear Map Projection]]
- [[Transformation Matrix]]
- [[Matrix Representation of Linear Rotation]]
- [[Set of All Linear Transformations Linear Combinations]]
- [[Standard Matrix]]