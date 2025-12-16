---
tags:
  - math
aliases:
  - Binomial Expansion
---
[[Pascals Theorem]]
This is using pascal triangle to expand binomials.
So a degree 3 binomial will match the coefficients with that row in the pascal's triangle.
# Shorthand notation
$(x+y)^n = \sum\limits_{i-0}^n  \binom{n}{i} x^{i}y^{n-i}$
### Corrolary
$$\sum_{r=0}^{n} \binom{n}{r} = 2^{n}$$
# Examples
### Example 1
$(x+y)^4$
4th row of pascal triangle: 1 4 6 4 1
$(x+y)^4 = x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + y^4$
### Example 2
$(1 + bx)^n = 1 - 3x + \frac{15}{4}x^2$
##### term 1:
$_{n}C_{0}(1)^n(bx)^0 = 1$
##### term 2:
$_{n}C_{1}(1)^{n-1}(bx)^1 = -3x$
$_{n}C_1 = \frac{n!}{n-1(1!)} = n$ 
$nbx = -3x$
$nb = -3$
$b=\frac{-3}{n}$
##### term 3:
$_{n}C_{2}(1)^{n-2}(bx)^2 = \frac{15}{4}x^2$
$=\frac{n!}{(n-2)!2!}b^2x^2 = \frac{15}{4}x^2$
$= \frac{(n)(n-1)}{2}b^2x^2 = \frac{15}{4}x^2$
$\frac{(n)(n-1)}{2}b^2 = \frac{15}{4}$
$\frac{(n)(n-1)}{2}\left( \frac{3}{n} \right)^2 = \frac{15}{4}$
$\frac{(n)(n-1)}{2}\left( \frac{9}{n^2} \right) = \frac{15}{4}$
$\frac{(9)(n-1)}{2n} = \frac{15}{4}$
$3b(n-1) = 30n$
$3bn-3b = 30n$
$6n = 3b$
$n = 6$
$b = -1/2$
