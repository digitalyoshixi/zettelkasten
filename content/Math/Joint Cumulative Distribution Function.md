---
tags:
  - math
  - statistics
  - probability
aliases:
  - Joint CDF
---
A [[Cumulative Distribution Function|CDF]] used to describe the joint distribution of [[Random Variable|RV]]
# Definition
$$F_{X,Y}(x,y) = P(X \leq x, Y \leq y) = P( \{ X\leq x \} \cap \{ Y \leq y \})$$
# Expressing [[Cartesian Product]] of intervals
With $B = (x_{1},x_{2}] \times[y_{1}, y_{2}) = \{ (x,y) : x \in (x_{1},x_{2}] \wedge y \in (y_{1},y_{2}] \} \subset \mathbb{R}^{2}$
Using Joint CDF directly, 
$P( (X,Y) \in B) = P(x_{1} < X \leq x_{2} , y_{1} < Y \leq y_{2}) = F_{X,Y}(x_{2},y_{2})-F_{X,Y}(x_{2},y_{1})-F_{X,Y}(x_{1},y_{2})-F_{X,Y}(x_{1},y_{1})$
