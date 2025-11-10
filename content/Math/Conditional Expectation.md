---
tags:
  - math
  - statistics
  - probability
---
A [[Functions of Random Variables]] $h(x) = E[Y|X=x]$.
# Definition
With [[Random Variable]] $X,Y$
The conditional expectation of $Y$ given the value of $X$ is:
$$
E[Y|X=x] = \begin{cases}
\sum_{y}yp_{Y|X}(y|x)\\ \\
\int_{-\infty}^{\infty} yf_{Y|X}(y|x)dy
\end{cases}
$$
### Intuition
The conditional expectation of $Y|X$ is the linear function of $X$ describing mean level of $Y$ based on $X$
![[Conditional Expectation-20251104162808782.webp]]
# Properties
- $Y \perp X \implies E(Y|X)=E(Y)$
- $E[g(X) \cdot Y|X] = g(X)E(Y|X)$
- $E[aY+bZ|X] = aE(Y|X)+bE(Z|X)$
- If $Y \perp X \implies E[Y \cdot Z | X] = E(Y|X) \times E(Z|X)$