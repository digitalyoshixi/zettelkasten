---
tags:
  - math
  - calculus
---
# Definition
A series $\sum a_{n}$ converges if:
- $\{ S_{n} \}$ converges
- Or, $\exists s \in \mathbb{R}, \lim_{ n \to \infty }S_{n} = s$
# Example
### Example 1
Does $\sum_{n=1}^{\infty} \ln\left( \frac{n+1}{n} \right)$ converge or diverge?
1. Note that $\sum_{n=1}^{\infty} \ln\left( \frac{n+1}{n} \right) = \sum_{n=1}^{\infty}[\ln(n+1) - \ln(n)]$
	1. Note, $S_{n} = a_{1} +a_{2} + \dots + a_{n-1} + a_{n}$
	2. $= \ln(n+1) - \ln(1)$ by [[Telescoping Series]]
	3. $= \ln(n+1)$
2. Then, $\lim_{ n \to \infty }S_{n} = \ln(\infty) = \infty$, and as $\infty$ is [[Not a Number|NaN]], then this limit [[Does Not Exist|DNE]]