---
tags:
  - math
  - linalg
---
# Theorem
- Let $T \in \mathcal{L}(V)$
- $dim(V) < \infty$
- Let $p(x)$ be the [[Minimal Polynomial]] with for $T$ with prime factorization $p(x) = p_{1}x^{r_{1}} * \dots * p_{k}x^{r_{k}}$ (in other words, $p_{j}$ are distinct irreducible monic polynomials and $r_{j} \geq 1$)
- Let $W_{j} = ker(p_{j}T^{r_{j}})$ for $j \in 1,\dots,k$
Then we get the properties:
1. $V = W_{1} \oplus \dots \oplus W_{k}$
2. $W_{i}$ is $T$-invariant for all $i$
3. if $T_{i}$ is a restriction to $W_{i}$, then $P_{i}^{r_{i}}$ is the [[Minimal Polynomial]] of $T_{i}$
# Properties
1. The minimal polynomial of each of the $T_{i}$ are a power of a single prime factor
2. If the characteristic polynomial has the same prime factors as the minimal polynomial, (i.e $f(x) = p_{i}(x)^{d_{1}} * \dots * p_{k}(x)^{d_{k}}$) then we can characterize the dimension
# Guides
- [[Primary Decomposition Theorem Example]]
# Proof
### Proving 1
- We show that $W_{1} + \dots + W_{k}$ is a [[Direct Sum]] by showing that $W_{i} \cap W_{j} = \{ 0 \}$ for all $i \neq j$
- Suppose $\alpha \in W_{i}$, and $\alpha \in W_{j}$. As $p_{i}$ and $p_{j}$ are [[Coprime]], then we know there exists polynomial $a$, $b$ such that $ap_{i} + bp_{j} = 1$
- This implies that $\alpha(T)p_{i}(T) + b(T)p_{j}(T) = I$
- So, $\alpha = I(\alpha) = \alpha (T)p_{i}(T)^{r_{i}}\alpha + b(T)p_{j}(T)^{r_{j}}\alpha$
- As $\alpha \in W_{i}i, W_{j}$, then: $\alpha = \alpha(T)0 + b(T)0 = 0$
- ...
### Proving 2
- Note that $p_{j}(T)$ commutes with$T$
- It follows immediately that $W_{j} = ker(p_{j}(T)^{r_{j}})$ is $T$-invariant
### Proving 3
- Let $T_{j}$ be the restriction of $T$ to $W_{j}$
- $p'$ is the minimal polynomial of $T_{j}$
- Since $W_{j} = ker(p_{j}(T)^{r_{j}})$, $p_{j}(x)^{r_{j}}$ annihilates $W_{j}$
- This, $p'|(p_{j}(x)^{r_{j}})$.
- This means that we can write $p_{j} = (p_{j}(x))^{k}$ for some $k \leq r_{i}$
![[Primary Decomposition Theorem-20250730143118554.webp]]