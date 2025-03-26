---
tags:
  - math
  - linalg
---
# Theorem
- Suppose $T(v_{i}) - \lambda_{i}v_{i}$ for $i = 1,\dots,n$ are distinct eigenvalues and eigenvectors of T
- The set of vectors $\{ v_{1} ,\dots,v_{n}\}$ is [[Linear Independence|Linearly Independent]]
# Proof
- Suppose for sake of contradiction that $\{ v_{1},\dots,v_{n} \}$ is dependent
- Then, there is a shortest possible dependence $0 = a_{1}v_{1} + .. + a_{k}v_{k}$ for $k \leq n$
- We apply $T$ to both sides and get
- $0 = T(0) = a_{1}T(v_{1}) + \dots + a_{k}T(v_{k})$
- $= a_{1}\lambda_{1}v_{1} + \dots + a_{k}\lambda_{k}v_{k}$
- We know that we have distinct eigenvalues.
- Therefore, there are atleast two values of $\lambda_{i}$ meaning $\exists \lambda_{k} \neq 0$
- Then, we divide out by that $\lambda_{k}$ to create a shorter dependence
- $0 = \frac{a_{1}\lambda_{1}}{\lambda _{k}}v_{1} +\dots + \frac{a_{k}\lambda_{k}}{\lambda_{k}}v_{k}$
- Then, we subtract our two equations
$a_{1}v_{1} + .. + a_{k}v_{k}- \frac{a_{1}\lambda_{1}}{\lambda _{k}}v_{1} +\dots + \frac{a_{k}\lambda_{k}}{\lambda_{k}}v_{k}$
- $= a_{1}(1-\frac{\lambda_{1}}{\lambda_{k}})v_{1} + ... + a_{k-1}(1-\frac{\lambda_{k-1}}{\lambda_{k}})v_{k}$
- We know that this equation is linearly dependent as some $a_{i}$ for $1 \leq i \leq k-1$ is non-zero. and $1- \frac{\lambda_{i}}{\lambda_{k}} = 0$
- Then, $\lambda_{i} = \lambda_{k}$. Then, there is no shortest dependence
- $\square$