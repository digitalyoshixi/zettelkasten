---
tags:
  - math
  - statistics
---
$$
\sum_{i}(X_{i} - \mu)^{2} = \sum_{i}(X_{i}-\overline X)^{2}+n(\overline X - \mu)^{2}
$$
# Proof
- $\sum_{i}(x_{i}-\mu)^{2} = \sum_{i}(x_{i}- \overline x + \overline x - \mu)^{2}$
- $= \sum_{i}(\overline x - \mu)^{2} + 2 \sum_{i}(x_{i}-\overline x)(x - \mu)$
- Note that with respect to $i$, $x_{i}$ is changing, $\overline x, \mu$ are constants
- $= \sum_{i}(x_{i}-\overline x)^{2} + n (\overline x - \mu)^{2} + 2(\overline x - \mu) \sum_{i}(x_{i} - \overline x)$
- Note that $\sum_{i}(x_{i}- \overline x) = 0$
- $= \sum_{i}(x_{i}-\overline x)^{2} + n (\overline x - \mu)^{2}$
- Re-arrange to get $\sum_{i}(x_{i}-\overline x)^{2} = \sum_{i}(x_{i} - \mu)^{2} - n(\overline x - \mu)^{2}$
- $\implies E[\sum_{i}(x_{i}-\overline x)^{2}] = E[\sum_{i}(x_{i} - \mu)^{2}] - nE[(\overline x - \mu)^{2}]$
- $\implies E[\sum_{i}(x_{i}-\overline x)^{2}] = \sum_{i}E[(x_{i} - \mu)^{2}] - nE[(\overline x - \mu)^{2}]$
- $\implies E[\sum_{i}(x_{i}-\overline x)^{2}] = V[x_{i}] - nV[\overline x]$
- $\implies E[\sum_{i}(x_{i}-\overline x)^{2}] = (n-1)(\sigma^{2})$
# Example
- [[Unbiasedness Identity for Sample Variance Statistic]]