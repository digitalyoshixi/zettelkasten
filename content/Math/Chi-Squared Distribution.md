---
tags:
  - math
  - probability
  - statistics
---
A [[Continuous Probability Distributions]] $\mathcal{X}^{2}$ for [[Gene|Genetics]].
- Let $U = Z^{2}$ where $Z$ is a [[Standard Normal Distribution|Standard Normal Variable]]
- $U \sum_{i=1}^{n} \mathcal{X}^{2}$ distribution with 1 degree of freedom written as $X_{(1)}^{2}$
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
# Properties
- Additive property: $X \sim \mathcal{X}_{(m)}^{2}$, $X \perp Y \implies X+Y \sim \mathcal{X}^{2}_{(m+n)}$
	- If $\mathcal{X}_{(m)}^{2} \equiv X_{(1)}^{2} + \dots + X_{(1)}^{2} = Z_{1}^{2} + \dots + Z_{(m)}^{2}$
- If $X \sim X_{(m)}^{2} \implies E[X] = m$