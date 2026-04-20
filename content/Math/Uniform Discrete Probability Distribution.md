---
tags:
  - math
  - distributions
aliases:
---
Occurs when in a single trial, all outcomes are equally likely.
- There are $n$ elements in $S$
- All outcomes $x$ have probability $P(x)=\frac{1}{n}$
- The sum of all probabilities in $S$ is $1$
$X \sim \mathcal{U}\{ a,b \}$
- $a$ is left endpoint
- $b$ is right endpoint
![[Uniform Discrete Probability Distribution-20241203165244513.webp]]
# PMF
$$p_{X}(x) = \frac{1}{n} $$
# CDF
- $x \in [a,b]$
$$
F_{X}(x) = \frac{x - a + 1}{n}
$$
# Expectation
$E(X) = \frac{a+b}{2}$
# Example
Random number generator between 1 and 5 inclusive.
P(X = x) = 1/5. each random number is equally likely and there is a single trial. So, this is a uniform distribution

To get the distribution, we will make a [[Frequency Table]] first:

| random number x | Probability P(X) | x \* P(x) |
| --------------- | ---------------- | --------- |
| 1               | 1/5              | 1/5       |
| 2               | 1/5              | 2/5       |
| 3               | 1/5              | 3/5       |
| 4               | 1/5              | 4/5       |
| 5               | 1/5              | 5/5       |

Expectation is the mean. But the formula is more suited to different cases. $\frac{1 + 2 + 3 + 4 + 5}{5} = 3$ 
