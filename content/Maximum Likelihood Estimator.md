---
tags:
  - math
  - statistics
aliases:
  - MLE
---
Estimator to find the most likely distribution a [[Statistic]] came from via a [[Likelihood Function]]
# Motivation
- With two distributions $P_{1}, P_{2}$ as [[Uniform Discrete Probability Distribution]]
- Under $P_{1}$, $X \sim \text{Uniform}(1,2,\dots,10^{3})$
- Under $P_{2}$, $X \sim \text{Uniform}(1,2,\dots,10^{6})$
- We observe one sample value of $X$ - say 10
- Which distribution did it come from?
- Which distribution is it more likely to have produced this random number
# Theorem
The likelihood that a [[Parameter]] came from a distribution is the distribution that has the highest likelihood value at the [[Likelihood Function]] at the given statistic.
![[Maximum Likelihood Estimator-20260113191851010.webp]]
# Properties
- MLE is not unique
- MLE may not exist
- Likelihood may not always be differentiable
	- Example: $X_{1}, \dots, X_{n} \sim_{iid} \text{Uniform}(0, \theta)$, in this case, $\hat{\theta}= max(x_{1},\dots,x_{n})$
	- We have to be careful when range of $X$ involves [[Parameter]] $\theta$
- [[Invariance Property of MLE]]
# Computation of MLE
- [[Likelihood Function]]
- [[Log-Likelihood Function]]
# Computation Example
Solve equation $\frac{\partial l(\theta)}{\partial \theta}$ for $X_{1},\dots,X_{n} \sim^{iid} \text{Poisson}(\lambda)$.
$P[X=x] = \frac{e^{-\lambda}\lambda^{x}}{x!}$
Then, $L(\lambda) = P[X_{1}=x_{1}] \times P[X_{2} = x_{2}] \times \dots \times P[X_{n} = x_{n}]$
$= \frac{e^{-\lambda}\lambda^{x_{1}}}{x_{1}!} * \dots * \frac{e^{-\lambda}\lambda^{x_{n}}}{x_{n}!}$
$= \frac{e^{-n \lambda}\lambda^{\sum_{i=1}^{n}x_{i}}}{\Pi_{i=1}^{n}x_{1}!}$