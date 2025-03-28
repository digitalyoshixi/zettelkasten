---
tags:
  - math
  - linalg
---
# Theorem
- Suppose $V$ is a $n$ dimensional $\mathbb{R}$ vector space with distinct $\mathbb{R}$ eigenvalues $\lambda_{1}, \lambda_{2}$
- If $S_{1} \subset E_{\lambda_{1}}$, $S_{2} \subset E_{\lambda_{2}}$ are sets of independent vectors
- Then, $S_{1} \cup S_{2}$  is independent
# Proof
1. Let $S_{1} = \{ u_{1} , \dots, u_{k} \}$ 
2. Let $S_{2} = \{ v_{k+1} ,\dots , v_{l} \}$
3. Suppose for the sake of contradiction that $S_{1} \cup S_{2} = \{ u_{1} ,\dots, u_{k}, v_{k+1}, \dots, v_{l} \}$ is dependent
4. Then, we have $a_{1}u_{1} + a_{k}u_{k} + \dots + a_{k+1}v_{k+1} + \dots + a_{l}v_{l} = 0$ s.t $a_{i} \neq 0$
5. One of the values $\lambda_{1} \neq \lambda_{2}$ must be non-zero. Assume $\lambda_{1} \neq 0$
6. First, note that $T(a_{1}u_{1} + \dots + a_{k}u_{k} + a_{k+1}v_{k+1} + \dots + a_{l}v_{l}) = T(0) = 0$
7. $\Longleftrightarrow a_{1}\lambda_{1}u_{1} + \dots + a_{k}\lambda_{1}u_{k} + a_{k+1}\lambda_{2}v_{k+1} + \dots + a_{l}\lambda_{2}v_{l} = 0$
8. We can mutliply the original dep by $\lambda_{1}$ and get:
   $a\lambda_{1}u_{1} + \dots + a_{1}\lambda_{1}u_{k} + a_{k+1}\lambda_{1}v_{k+1} + \dots + a_{l}\lambda_{1}v_{l} = 0$
9. Then, $a_{1}\lambda_{1}u_{1} + \dots + a_{k}\lambda_{1}u_{k} + a_{k+1}\lambda_{2}v_{k+1} + \dots + a_{l}\lambda_{2}v_{l} - a\lambda_{1}u_{1} + \dots + a_{1}\lambda_{1}u_{k} + a_{k+1}\lambda_{1}v_{k+1} + \dots + a_{l}\lambda_{1}v_{l}= a_{k+1}(\lambda_{2}-\lambda_{1})v_{k+1} + \dots + a_{l}(\lambda_{2}-\lambda_{1})v_{l} = 0$
10. This means that $a_{k+1}(\lambda_{2}-\lambda_{1})v_{k+1} + \dots + a_{l}(\lambda_{2}-\lambda_{1})v_{l} = 0$
11. Note that $\lambda_{2} - \lambda_{1} \neq 0$
12. Thus, this gives a dependence for vectors $\{ v_{k+1}, \dots ,v_{l} \}$. This contradicts that $S_{2}$ is a linearly independent set.
13. Thus, $S_{1} \cup S_{2} = \{ u_{1} ,\dots, u_{k}, v_{k+1}, \dots, v_{l} \}$ is [[Linear Independence|indep]]