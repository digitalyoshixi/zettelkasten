---
tags:
  - math
  - probability
  - statistics
---
The ratio between the [[Standard Normal Distribution]] and [[Chi-Squared Distribution]].
# Definition
If $Z \sim N(0,1)$ and $V \sim \mathcal{X}^{2}(n)$ with $Z \perp V$,
Then $T = \frac{Z}{\sqrt{ \frac{V}{n} }}$ follows a t-distribution with degrees of freedom $n$.
# Sample Mean and Variance
$$
\frac{\frac{\overline X_{n} - \mu}{\sqrt{ \frac{\sigma^{2}}{n} }}}{\sqrt{ \frac{S^{2}_{n}}{\sigma^{2}} }}
=
\frac{\overline X_{n} - \mu}{\sqrt{ \frac{S_{n}^{2}}{n} }}
\sim t(n-1)
$$
# Properties
$T = \frac{Z}{\sqrt{ V/n }} \sim t_{(n)} \implies T^{2} = \frac{Z^{2}}{\frac{V}{n}} \sim F(1,n)$