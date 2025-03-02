---
tags:
  - math
  - linalg
---
# Theorem
- Suppose $T : V \to W$
- Suppose $dim(V) = dim(W) = n < \infty$ (T is linear)
- T is [[Injective Functions|Injective]] $\Longleftrightarrow$ T is [[Surjective Functions|Surjective]]
# All or Nothing Matrix
![[Drawing 2025-02-26 09.58.56.excalidraw]]
# Proof
1. [[Rank Nullity Theorem]] says $dim(V) = dim(Image(T)) + dim(ker(T))$
2. Suppose $T$ is injective, thus we get $dim(ker(T)) = 0$
	1. $dim(W) = dim(V) = dim(Image(T)) = 0$
	2. Therefore, $T$ is surjective
3. Suppose $T$ is surjective, then we get $dim(Image(T)) = dim(W)$
	1. $dim(W) = dim(V) = dim(W) + dim(Ker(T))$
	2. $\implies dim(Ker(T)) = 0$ 
	3. Therefore, $T$ is injective
