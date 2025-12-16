---
tags:
  - statistics
  - probability
aliases:
  - Conditional PDF
---
A probability density function for [[Continuous Random Variable|Continuous RV]] $X,Y$ defined as:
$$f_{X|Y} (x|y) = \frac{f_{X,Y(x,y)}}{f_{Y}(y)}$$
# Properties
- Conditional PDF is a proper [[Probability Density Function|PDF]]
- $f_{X|Y}(x|y) = \int_{A} f_{X|Y}(x|y)dx, \forall A \subset \mathbb{R}$
- $f_{X,Y}(x,y) = f_{X}(x)f_{Y|X}(y|x), \forall x,y$ ([[Multiplication Rule of Probability]])