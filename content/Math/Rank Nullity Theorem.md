---
tags:
  - math
  - linalg
aliases:
  - Dimension Theorem
---
- If $V,W$ are finite dimensional vector spaces and $T : V\to W$ is linear
- Then: $dim(ker(T))+dim(Image(T)) = dim(V)$
- or, $dim(V) = nullity(T) + rank(T)$
# Proof
1. Refer to the proof of [[Bases for Images and Kernel Procedure 2]]
2. Then, we need to show $\{ T(v_{k+1}),\dots,T(v_{n}) \}$ is a basis
3. Checking linear independence:
	1. Suppose for sake of contradiction that $0 = a_{k+1}T(v_{k+1})+\dots+a_{n}T(v_{n})$ has some non-zero coefficient $a_{z} \neq \hat0$
	2. This gives: $\overrightarrow{0} = T(\overrightarrow{0}) = T(a_{k+1}v_{k+1}+\dots+a_{n}v_{n})$
	3. Therefore $a_{k+1}v_{k+1} + \dots+a_{n}v_{n} \in ker(T)$u
	4. But we already have a basis for $ker(T) = \{ b_{1}u_{1},\dots,b_{k}u_{k} \}$
	5. $\implies a_{k+1}v_{k+1} + \dots +a_{n}v_{n} = b_{1}u_{1} + \dots +b_{k}u_{k} + 0v_{k+1} + \dots + 0v_{n}$
	6. Note that this gives us a non-unique representation in the basis $\{ u_{1}, u_{k},\dots,v_{k+1},\dots,v_{n} \}$
	7. $\{ T(v_{k+1}),\dots,T(v_{n}) \}$ is a [[Linear Independence|indep]]
# Use Cases
- [[Examples of Rank Nullity]]
