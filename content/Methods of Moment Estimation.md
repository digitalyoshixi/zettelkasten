---
tags:
  - math
  - statistics
aliases:
  - MME
---
We can approximate the [[Moment|Population Moment]] with [[Sample Moment]].
$$
\frac{1}{n}\sum_{i=1}^{n}X_{i}^{k} \sim E[X^{k}]
$$
# Summary
- Express lower order population moments in terms of parameters
- Invert expressions to express parameters in terms of population moments
- Replace the population moments with sample moments
# Example
For $X_{1},\dots,X_{n} \sim^{iid} \text{Poisson}(\lambda)$, find the method of moments estimator of $\lambda$.
$X_{i} \sim \text{Poisson}(\lambda)$
$\lambda = E[X]$
MGF estimation of $\lambda$, $\lambda = \frac{1}{n}\sum_{i=1}^{n}X_{i} = \overline X$
