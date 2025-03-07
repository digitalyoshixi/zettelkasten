---
tags:
  - math
  - linalg
---
# Theorem
- Suppose $V, W$ are finite dimensional vector spaces
- If $dim(V) < dim(W)$
- Then, $T: V\to W$ is not surjective
# Intuition
There is no surjective linear transformation $R^{2} \to R^{100}$
# Proof
- The rank-nullity theorem says: $dim(V) = dim(Image(T)) + dim(Ket(T))$
- $\implies dim(V) \geq dim(Image(T))$ By whole numbers
- $\implies dim(W) > dim(V) > dim(image(T))$
- $\implies dim(W) > dim(Image(T))$
- Therefore, $dim(W) \neq dim(Image(T))$
- And thus, $T$ is not surjecitive1
