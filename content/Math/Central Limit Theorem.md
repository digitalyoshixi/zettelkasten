---
tags:
  - math
  - probability
  - statistics
aliases:
  - CLT
---
# Definition
The [[Standardized Average]] of [[Independent Random Variable]] with finite means and variance converge to [[Normal Distribution]] $\text{Normal}(0,1)$
# Formal Definition
$$Z_{n} = \sqrt{ n } \left( \frac{\overline X_{n}-\mu}{\sigma} \right) \to_{D} \text{Normal}(0,1) \Longleftrightarrow \overline X_{n} \sim_{appr} N(\mu, \frac{\sigma^{2}}{n})$$
# Normal Curve Definition
$\lim_{ N \to \infty } P\left( a < \frac{\overline X_{n} - N*\mu}{\sigma * \sqrt{ N }} < b\right ) = \int_{b}^{a} \frac{1}{\sqrt{ 2 \pi }}e^{-x^{2}/*2*}dx$
# Central Limit Theorem Approximation Example
![[Central Limit Theorem-20251218041013746.webp]]