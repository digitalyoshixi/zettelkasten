---
tags:
  - math
  - probability
  - statistics
---
A [[Continuous Probability Distributions]] for [[Gene|Genetics]].
# Definition
With $Z_{1}, \dots, Z_{n} \sim_{iid} N(0,1)$, then:
$$
\begin{cases}
Z_{1}^{2} \sim \Gamma(\frac{1}{2}, \frac{1}{2}) = \mathcal{X}^{2}(1)\\
Z_{1}^{2} + \dots + Z_{n}^{2} \sim \Gamma(\frac{1}{2}, \frac{1}{2}) = \mathcal{X}^{2}(n)\\
\end{cases}
$$
# Sampling Distribution
$$
\frac{(n-1)S^{2}_{n}}{\sigma^{2}} = \frac{\sum_{i=1}^{n}(X_{i} - \overline X_{n})^{2}}{\sigma^{2}} \sim \mathcal{X}^{2}(n-1)
$$