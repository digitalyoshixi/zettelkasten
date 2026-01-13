---
tags:
  - math
  - statistics
---
Estimator to find the most likely distribution a [[Statistic]] came from.
# Motivation
- With two distributions $P_{1}, P_{2}$ as [[Uniform Discrete Probability Distribution]]
- Under $P_{1}$, $X \sim \text{Uniform}(1,2,\dots,10^{3})$
- Under $P_{2}$, $X \sim \text{Uniform}(1,2,\dots,10^{6})$
- We observe one sample value of $X$ - say 10
- Which distribution did it come from?
- Which distribution is it more likely to have produced this random number
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