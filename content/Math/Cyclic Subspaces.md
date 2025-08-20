---
tags:
  - math
  - linalg
---
The subspace comprised of compositions of transform on the same vector, wherein a certain step in the transformation process will return back a [[Linear Combination]] of the initial vector.
Used to assist in finding the matrix representation of a characteristic polynomial.
# Definition
1. For a non-zero [[Vector|Vector]] $v$
2. For the smallest $k$ that allows for $\{ v, T(v), T^{2}(v),\dots, T^{k}(v) \}$
3. The cyclic subspace is $C_{v} = \{ v, T(v), T^{k-1}(v) \}$
### Alternate Definition
- With $\alpha \in V$ and $p$ be the [[T-Annihilator of a Vector|T-Annihilator]] of $\alpha$
- Let $deg(p) = k$
Then,
1. $\{  \alpha, T(\alpha), \dots, T^{k-1}\alpha \}$ is $T$ [[Invariant]]
2. $span \{ \alpha, T\alpha, \dots, T^{k-1}\alpha \}$ is T [[Invariant]]
The set $Z(\alpha_{j}T) =span \{ \alpha, T\alpha, \dots, T^{k-1}\alpha \}$ is the cyclic subspace of $\alpha$
# Theorems
- [[Cyclic Decomposition Theorem]]
- [[Cyclic Subspace Corrolary]]
- [[Matrix Definition of Cyclic Subspace]]
# Proof
### Proving Independence
- Suppose for sake on contradiction that $\{  \alpha, T\alpha, \dots, T^{k-1}\alpha \}$ is [[Linear Independence|Linearly Dependent]]
- Then, there exists a non-trivial linear combination equal to zero ($a_{k-1}T^{k-1}\alpha + \dots + a_{0}a = 0$)
- let $p(x) -= \alpha_{k-1}x^{k-1} + \dots + \alpha_{0}$, then $p(T)\alpha = 0$
- This contradicts that $p$ being the $T$ annihilator of $\alpha$ as it also annihilates up to $k$, thus $\{  \alpha, T\alpha, \dots, T^{k-1}\alpha \}$ is [[Linear Independence|indep]]
### Proving $T$ invariant
- As $T^{j}\alpha \in W$ for all $j < k$
- We need to show $T^{k}\alpha \in span \{ \alpha, T\alpha, \dots, T^{k-1}\alpha \}$
- As $p(T)\alpha = 0$ then, $T^{k}\alpha + \alpha_{k-1}T^{k-1} \alpha \dots+ \alpha_{0}I \alpha = 0$
- $\implies T^{k} \alpha \in span \{ \alpha, \dots, T^{k-1}\alpha \}$
- Thus, $\{  \alpha , \dots, T^{k-1}\alpha\}$ is $T$-[[Invariant]]