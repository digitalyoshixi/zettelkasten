---
tags:
  - math
  - linalg
---
# Theorem
1. Let $T \in \mathcal{L}(V)$
2. Let $dim(V) = n < \infty$
Then, 
3. $T$ is [[Upper Triangular Matrices|Triangularizable]] $\Longleftrightarrow$ the [[Prime Factorization]] of the [[Minimal Polynomial]] for $T$ is a product of linear factors
4. $T$ is [[Diagonal Matrices|Diagonalizable]] $\Longleftrightarrow$ the [[Prime Factorization]] of the [[Minimal Polynomial]] for $T$ is a product of **distinct** linear factors
# Proof
### Proving Triangular Case
1. Suppose $T$ is [[Upper Triangular Matrices|Triangular]] with basis $\beta$
2. Then, the [[Characteristic Polynomial]] of $T$ is $\det(xI - [T]_{\beta}) = f(x) = (x- a_{11})(x-a_{22})\dots(x-a_{nn}) = (x-c_{1})^{d_{1}} \dots (x-c_{k})^{d_{k}}$
   Where $a_{i}$ are distinct characteristic values. Therefore, the minimal polynomial for $T$ has similar form since it divides $f(x)$ by [[Cayley Hamilton Theorem]]
##### Proving $\implies$Triangularizability
1. If $[T]_{\beta}$ is diagonal, then $p(x) = (x-c_{1}) \dots (x-c_{k})$ is the minimal polynomial for $T$
2. Then, $p(T) = (T-c_{1})\dots(T-c_{k}) = 0$ as each diagonal entry will be multiplied by $0$ at some point
##### Proving $\Longleftarrow$ Triangularizability
1. Suppose the minimal polynomial is a product of  linear factors. Apply the previous lemma to $W = \{  0 \}$ to get $\alpha _1$
2. Then, $(T - eI)\alpha_{1} = 0 \implies T \alpha_{1} = c \alpha_{1} \in span(\{  \alpha_{1} \})$
3. Let $W_{1} = span( \{  \alpha_{1} \})$. Note that $W_{1}$ is $T$-invariant.
4. We can apply the previous lemma to $W_{1}$ to get $\alpha_{2}$.
5. Then, $(T - e)\alpha_{2} = 0\implies T\alpha_{2} = c_{1} \alpha_{1} + c_{2} \alpha_{2} \in span(\{ \alpha. \alpha_{2} \})$
6. Continue this way until you have $W_{n} = V$ ([[Linear Independence Extension Lemma]])
7. Let $\beta = \{ \alpha_{1},\dots, \alpha_{n} \}$. Then, $[T]_{\beta}$ is [[Upper Triangular Matrices|Upper Triangular]]
### Proving Diagonizable Case
##### Proving $\Longleftarrow$ Diagonalizability
1. Suppose that $T$ is not diagonal for sake of contradiction
2. Suppose $W$ is the subspace spanned by all [[Eigenvector|Characteristic Vector]] of $T$.
3. If $W = V$, then $T$ is diagonizable, as proven earlier.
4. This contradicts our assumption
5. Instead, consider $W = V$
6. By the previous lemma, there exists a vector $\alpha$ not in $W$ and a characteristic value $c_{i}$ of $T$ such that the vector $\beta = (T - c_{i}I) \alpha \in W^{*}$
7. Let $h(T)$ be some polynomial
8. We will find $h(T) \in W$
9. Now, $p = (x-c_{i})(q_{i})$ for some polynomial $q$
10. We pick $h$ s.t $q - q({ci}) = (x - c_{i})h$
11. Thus, we have that $q(T) \alpha = q(c_{i})\alpha = h(T)(T - c_{i}) \alpha = h(T)\beta$
12. As $0 = p(T) \alpha = (T - cI)q(T)\alpha$, the vector $q(T) \alpha$ is an [[Eigenvector]] as long as $q(T)\alpha \neq 0$. This implies that $q(T)\alpha = \lambda \alpha, \lambda \in \mathbb{F}$
13. This implies that $q(T) \alpha - q(c_{i})\alpha = k\alpha = h(T)\beta \in W$
14. Thus, $\alpha \in W$
15. As $\alpha \in W$ , as $q(c_{i}) \alpha = q(T) \alpha \in W$, then $q(c_{i}) = 0$
16. By [[Remainder Theorem|Fundamental Remainder Theorem]], $c_{i}$ is a root of $q$. Thus, $p$ has a repeated root in $c_{i}$ for the minimal polynomial has a non-linear factor.
##### Proving $\implies$ Diagonalizability