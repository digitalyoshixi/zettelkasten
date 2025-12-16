---
tags:
  - math
  - distributions
  - continuous_probability
aliases:
  - Bell Curve
  - Gaussian Distribution
---
A type of [[Continuous Probability Distributions]]
Best used to model an average of independent RVs.
This distribution can be modelled with the [[Density Function]]
![[Normal Distribution-20250930143421667.webp]]
# [[Probability Density Function|PDF]]
$$f(x)= \frac{1}{\sqrt{ 2 \pi \sigma }}\exp \left\{  -\frac{1}{2} (\frac{x - \mu}{\sigma})^{2} \right\}, x \in \mathbb{R}$$
With:
- $\sigma$ as [[Standard Deviation]]
- $\mu$ as [[Expectation|Mean]]
- $\text{exp}$ is [[Euler's Number|Exponential Function]]
# CDF
$$
F(x) = \frac{1}{2}[1+\text{erf}(\frac{x-\mu}{\sigma \sqrt{ 2 }})]
$$
# [[Expectation]]
$$E(X) = \mu$$
# [[Variance]]
$$V(X)= \sigma^{2}$$
# [[Moment Generating Function|MGF]]
$$
\exp \{ ut + \frac{1}{2} \sigma^{2}t^{2} \}
$$
# Concepts
- [[Standard Normal Distribution]]
- [[Normal Distribution Standard Deviation Approximation]]
- [[68,95,99.7 Rule]]