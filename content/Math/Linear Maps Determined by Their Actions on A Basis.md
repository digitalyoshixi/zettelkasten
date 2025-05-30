---
tags:
  - math
  - linalg
---
Suppose $V$ is a finite dimensional vector space with basis $\alpha = \{ v_{1}, \dots, v_{n} \}$
If $S : V \to W$ and $T : V \to W$ are [[Linear Transform|Linear Maps]] s.t $S(v_{1}) = T(v_{1})$
For each $v_{i}$ in the basis $\alpha$, then $S(v) = T(v)$ for all $v \in V$
# Intuition
![[Linear Maps Determined by Their Actions on A Basis-20250211032359223.webp]]
Every transformed vector in a linear map is determined based off its basis vectors
# Proof
Suppose $T(v_{i}) = S(v_{i})$ for all $v_{i} \in \alpha$
Pick any vector $v \in V$
We can represent $v$ uniquely using the basis $\alpha$ as $v = \alpha v_{1} + \dots + a_{n}v_{n}$
Where: $a_{i} \in F$ and $v_{i} \in \alpha$.
This gives: $S(v) = S(a_{1}v_{1}+ \dots + a_{n}v_{n})$
$= a_{1}S(v_{1}) + \dots + a_{n}S(v_{n})$
$= a_{1}T(v_{1}) + \dots + a_{n}T(v_{n})$ as $S(v_{i} ) = T(v_{i})$
$= T(a_{1}v_{1} + \dots + a_{n}v_{n})$
$= T(v)$
Therefor: $S(v) = T(v)$ for all $v \in V$
$$\square$$