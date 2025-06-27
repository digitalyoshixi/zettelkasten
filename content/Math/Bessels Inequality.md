---
tags:
  - math
  - linalg
---
Often used to find a lower bound for a function.
Heavily used in optimization.
# Corrolary
- let $\{ \alpha_{1} ,\dots, \alpha_{n} \}$ be an orthogonal set of non-zero vectors in an [[Inner Product Space]]
- If $\beta$ is any vector in $V$
- Then, $\sum_{i=1}^{n} \frac{ | \langle \beta | \alpha_{k} \rangle|^{2}}{| | \alpha_{k}|| ^{2}} \leq || \beta ||^{2}$
	- With equality $\Longleftrightarrow \beta = \sum_{i=1}^{n} \frac{ | \langle \beta | \alpha_{k} \rangle |^{2}}{|| \alpha_{k}|| ^{2}} \alpha_{k}$
# Proof
1. Let $g = \sum_{i=1}^{n} \frac{ | \langle\beta | \alpha_{k} \rangle |^{2}}{|| \alpha_{k}||^{2}}\alpha_{k}$ and $\delta = \beta - \gamma$
2. Then, $\beta = \alpha + \delta$ by definition of $\gamma$, $\langle \delta | \gamma \rangle = 0$
3. Then, by [[Generalized Pythagorean Theorem]] $|| \beta || ^2 = || \gamma || ^2 + || \delta || ^2$
4. By definition of $\gamma$, $|| \gamma ||^{2} = \sum_{i=1}^{n} \frac{| \langle \beta | \alpha_{2}  \rangle ^{2} |}{ || \alpha_{k} || ^{2}} \leq || \gamma ||^{2} + || \delta || ^2 = ||\beta||^{2}$, with equality $\Longleftrightarrow ||  \delta||^{2 = 0}$
5. It is now sufficient to show $|| \delta || = \sum_{i=1}^{n} \frac{| \langle \beta | \alpha_{k} \rangle | ^{2}}{|| \alpha_{k}||^{2}}$
