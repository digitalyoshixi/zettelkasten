---
tags:
  - math
  - calculus
---
# Definition
A series $\sum a_{n}$ converges if:
- The series of [[Series Partial Sum|Partial Sums]] $\{ S_{n} \}$ converges
- Or, $\exists s \in \mathbb{R}, \lim_{ n \to \infty }S_{n} = s$
# Proving Series
- By definition
- [[Integral Test]]
- [[Series Divergence|Div Test]]
- [[Geometric Series Convergence|GS Test]]
- [[P-Series Test]]
- [[Direct Comparison Theorem]]
# Properties
### Additive Property
1. If $\sum a_{n}$ converges to $c$
2. If $\sum b_{n}$ converges to $s$
3. Then. $\sum(a_{n} + b_{n})$ converges to $c + s$
### Constant Multiple Property
1. If $\sum a_{n}$ converges to $c$
2. Then, $\sum k a_{n}$ converges to $kc$
### Vanishing Condition
1. If $\sum a_{n}$ converges to $c$
2. Then, as we approach the infinite-th term of the set, $\lim_{ n \to \infty }a_{n} = 0$
[[Proof of Series Vanishing Condition]]
##### Intuition
- In order to have a sum that is a constant, all the elements of the set must be infinitesimally small
# Example
### Example 1
Does $\sum_{n=1}^{\infty} \ln\left( \frac{n+1}{n} \right)$ converge or diverge?
1. Note that $\sum_{n=1}^{\infty} \ln\left( \frac{n+1}{n} \right) = \sum_{n=1}^{\infty}[\ln(n+1) - \ln(n)]$
	1. Note, $S_{n} = a_{1} +a_{2} + \dots + a_{n-1} + a_{n}$
	2. $= \ln(n+1) - \ln(1)$ by [[Telescoping Series]]
	3. $= \ln(n+1)$
2. Then, $\lim_{ n \to \infty }S_{n} = \ln(\infty) = \infty$, and as $\infty$ is [[Not a Number|NaN]], then this limit [[Does Not Exist|DNE]]
