---
tags:
  - math
  - linalg
---
# Theorem
- With $dim(V) = n < \infty$
- With $dim(W) = m < \infty$
- $dim(\mathcal{L}(V,W)) = nm$
# Proof
1. With $\beta = \{ a_{1},\dots,a_{n} \}$ for $V$
2. With $\beta' = \{ b_{1},\dots,b_{m} \}$ for $W$
3. For each pair $(p,q)$ where $p \in [1,n], q \in [1,m]$
	1. Define a [[Linear Transform|Linear Map]] $E^{p,q} \in \mathcal{L}(V,W)$
	2. $$
E^{p,q}(a_{i}) = \begin{cases} 
          b_{p} & i = q \\
          0 & i \neq q 
       \end{cases}
$$
4. Note that $\{ E^{p,q} | p \in [1,n], q \in [1,m] \}$ forms a basis for $\mathcal{L}(V,W)$
5. Thus, $dim(\mathcal{L}(V,W)) = n * m$
