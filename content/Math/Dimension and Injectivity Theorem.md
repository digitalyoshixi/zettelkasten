---
tags:
  - math
  - linalg
---
- Suppose that $V,W$ are finite dimensional vector spaces
- If $dim(W) < dim(V)$
- Then, $T:V\to W$ is not [[Injective Functions|Injective]]
# Intuition
There is no injective linear transformation of $T:R^{100} \to R^{2}$ that remains injective
# Proof
- The [[Rank Nullity Theorem]] gives: $dim(T) = dim(Ker(T)) + dim(Image(T))$
- $\implies dim(T) = dim(Ker(T)) + dim(W)$ as $Image(T) = W$
- Note that $dim(W) < dim(V)$ by assumption
- Thus, $\implies 1 \leq dim(ker(T))$
- This means we are guaranteed some non-zero vector in the kernel. $ker(T) \neq \{ \overrightarrow{0}v \}$ 
- Thus, $T$ is not injective