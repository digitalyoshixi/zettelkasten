---
tags:
  - math
  - statistics
---
# Definition
With $X_{1}, \dots, X_{n}$ as a  [[Joint Probability Mass Function]] or [[Joint Probability Density Function|Joint PDF]]
With observed samples $X_{1} = x_{1}, \dots,X_{n}=x_{n}$
The likelihood function $L(\theta|x_{1},\dots,x_{n}) = f(x_{1},\dots,x_{n}|\theta)$
Can be calculated as:
$$L(\theta) = \Pi_{i=1}^{n}f_{\theta}(x_{1})$$

# Example
For [[Bernoulli Trials]] $0 < \theta < 1$
We flip coins, and we observe [[Independent and Identically Distributed Random Variables|IID]] sample $(1,0,1,1,0)$
$L(\theta|X_{1}=1, X_{2}=0,X_{3}=1,X_{4}=1,X_{5}=0)$
$=\theta^{3}(1-\theta)^{2}$
Note that this is the probability of getting the sample $(1,0,1,1,0)$.