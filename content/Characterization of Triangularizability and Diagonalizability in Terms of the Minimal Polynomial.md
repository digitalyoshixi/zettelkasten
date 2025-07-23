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
1. Suppose $T$ is [[Upper Triangular Matrices|Triangular]] with basis $\beta$
2. Then, the [[Characteristic Polynomial]] of $T$ is $\det(xI - [T]_{\beta}) = f(x) = (x- a_{11})(x-a_{22})\dots(x-a_{nn}) = (x-c_{1})^{d_{1}} \dots (x-c_{k})^{d_{k}}$
   Where $a_{i}$ are distinct characteristic values. Therefore, the minimal polynomial for $T$ has similar form since it divides $f(x)$ by [[Cayley Hamilton Theorem]]
### Proving $\implies$
1. If $[T]_{\beta}$ is diagonal, then $p(x) = (x-c_{1}) \dots (x-c_{k})$ is the minimal polynomial for $T$
2. Then, $p(T) = (T-c_{1})\dots(T-c_{k}) = 0$ as each diagonal entry will be multiplied by $0$ at some point
### Proving $\Longleftarrow$
1. Suppose the minimal polynomial is a product of  linear factors. Apply the previous lemma to $W = \{  0 \}$ to get $\alpha _1$
2. Then, $(T - eI)\alpha_{1} = 0 \implies T \alpha_{1} = c \alpha_{1} \in span(\{  \alpha_{1} \})$
3. Let $W_{1} = span( \{  \alpha_{1} \})$. Note that $W_{1}$ is $T$-invariant.
4. We can apply the previous lemma to $W_{1}$ to get $\alpha_{2}$.
5. Then, $(T - e)\alpha_{2} = 0\implies T\alpha_{2} = c_{1} \alpha_{1} + c_{2} \alpha_{2} \in span(\{ \alpha. \alpha_{2} \})$
6. Continue this way until yo