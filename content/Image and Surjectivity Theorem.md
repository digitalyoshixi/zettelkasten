---
tags:
  - math
  - linalg
---
- Let $T : V\to W$ be a linear transformation
- Suppose $W$ is a finite dimensional vector space
- Then, the following are equivalent
	1. $T$ is [[Surjective Functions|Surjective]]
	2. $Image(T) = W$
	3. $dim(Image(T)) = dim(W)$
# Proof
### Proving $1 \implies 2$
- Suppose $T$ is surjective
- By defn of $Image(T)$, we know $Image(T) \subset W$
- We now argue that $W \in Image(T)$
	- Pick arbitrary $w \in W$, by defn of surjective
	- There is $\overrightarrow{v} \in V$ s.t $T(\overrightarrow{v}) = \overrightarrow{w}$
	- Therefore, $\overrightarrow{w} \in Image(T)$
	- Thus, $W \subset Image(T)$
	- Thus, $Image(T) = W$
### Proving $2 \implies 3$
- Suppose $Image(T) = W$
- Thus, $dim(Image(t)) = dim(W)$ (note that we need to be finite dimensional for this to be defined)
### Proving $3 \implies 1$
- Suppose $dim(Image(T)) = dim(W)$
- Show that $T$ is surjective
- By [[Subspace Finite Dimensional Vector Space Lemma]], they are equal