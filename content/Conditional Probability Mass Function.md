---
tags:
  - statistics
  - probability
aliases:
  - Conditional PMF
---
For [[Discrete Random Variable]] $X$, $Y$, 
$$P((X,Y) \in A | (X,Y) \in B) = \sum_{(x,y) \in A}P(X = x, Y=y|(X,Y) \in B)$$
Where:
- $P(X = x, Y=y|(X,Y) \in B) = \frac{P(\{  X = x, Y = y \} \cap \{ (X,Y) \in B \})}{P( (X,Y) \in B)}$
represents the conditional PMF of $X,Y$ given $(X,Y) \in B$
# One-Variable PMF
$$p_{X|Y}(x|y) = P(X=x|Y=y) = \frac{P(X=x,Y=y)}{P(Y=y)} = \frac{p_{X,Y}(x,y)}{p_{Y}(y)}$$
# Defining [[Joint Probability Mass Function|Joint PMF]]
$$P(X=x,Y=y) = P(X=x)P(Y=y|X=x), \forall x,y$$