---
tags:
  - math
  - linalg
---
- Let $T: V\to W$ be a linear map
- Then, the following are equivalent:
	1. $T$ is injective
	2. $ker(T) = {0v}$
	3. $dim(ker(T)) = 0$
# Proof
### Proving $1 \implies 2$
- Suppose $T:V\to W$ is linear and injective.
- We know $\{ \overrightarrow{0}v \} \subset ker(T)$ because $T(\overrightarrow{0}v) = \overrightarrow{0}w$ for all linear maps
- Suppose $\overrightarrow{v} \in ker(T)$. This gives: $\overrightarrow{0}w = T(\overrightarrow{v}) = T(\overrightarrow{0}v)$
- Since $T$ is injective, we get $v = \overrightarrow{0}v$
- Thus, $ker(T) \subset \{  \overrightarrow{0}v \}$
- Thus, $ker(T) = \{ \overrightarrow{0}v \}$
### Proving $1 \implies 3$
- Suppose $ker(T) = \{ \overrightarrow{0}v \} = span(\emptyset)$
- Thus, $\emptyset$ is a basis of $ker(T)$
- It follows that $dim(ker(T)) = 0$
### Proving $3 \implies 1$
- Suppose $dim(ker(T)) = 0$
- Therefore, $\emptyset$ is a basis of $ker(T)$
- This gives $ker(T) = span(\emptyset) = \{ \overrightarrow{0}v \}$
- Now, we argue that $T$ is injective
	- Suppose $T(\overrightarrow{x}) = T(\overrightarrow{y})$
	- $\Longleftrightarrow T(x) - T(y) = 0$
	- $\Longleftrightarrow T(x-y) = \overrightarrow{0}$ by linearity
	- Thus, $x-y \in ker(T) = \{ \overrightarrow{0}v \}$
	- Thus, $x-y = \overrightarrow{0}v \implies x = y$
	- It follows that $T$ is injective