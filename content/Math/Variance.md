---
tags:
  - math
  - statistics
---
The [[Weighted Means]] described by the distribution of a [[Random Variable]].
It is the 2nd degree [[Central Moment]].
Describes spead/average of squared distances from mean.
# Formula
$V(X)=E((X-E(X))^{2}) =E(X^{2})-E(X)^{2}$
- $\mu$ is $E(X)$ [[Expectation|Mean]]
# Alternate Formula
Square of the [[Standard Deviation]]. Aka SD without the square root.
$$V(X) = \sigma^{2}$$
# Specifics
- [[Law of Total Variance]]
# Properties
- $V(aX) = a^{2}V(X)$
# Example
- Sample of two people
- Probability $60 \%$ that a person approves of the president
- Random variable describing how many people approve
- Find expectation.
First, [[Random Variable]] $X \mapsto \{ 0,1,2 \}$
We can write out the distribution:

| x   | p(x)                   |
| --- | ---------------------- |
| 0   | $0.4 * 0.4 = 0.16$     |
| 1   | $0.4 * 0.4 * 2 = 0.48$ |
| 2   | $0.6 * 0.6 = 0.36$     |
We find [[Expectation]] $E(X) = 0.16*0 + 0.48*1 + 0.36*2 = 1.2$
$E[(X-\mu)]^{2} = \sum_{i=1}^{n}(x_{i}-\mu)^{2}p(x_{i})$
$=(-1.2)^{2}(0.16) + (-0.2)^{2}(0.48)+(0.8)^{2}(0.36) = 0.48$