---
tags:
  - math
  - calculus
aliases:
  - Dr Peyams Trick
---
A technique to save time for [[Integration by Parts]] by adding a constant to $v$
# Example
$$\int x \arctan(x) dx$$
Choose $u = \arctan(x), v' = x$
$\implies u' = \frac{1}{x^{2}+1}dx$
$\implies v = \frac{1}{2}x^{2} + \frac{1}{2}$ (Important step, we added the constant $\frac{1}{2}$)
Apply [[Integration by Parts]]
$= (\frac{1}{2}x^{2} + \frac{1}{2})\arctan(x) - \int (\frac{1}{2}x^{2} + \frac{1}{2})(\frac{1}{x^{2}+1})dx$
$= \frac{1}{2}\arctan(x)x^{2} + \frac{1}{2}\arctan(x) - \int \frac{1}{2}(x^{2} + 1)(\frac{1}{x^{2}+1})dx$
$= \frac{1}{2}\arctan(x)x^{2} + \frac{1}{2}\arctan(x) - \int \frac{1}{2}(1)dx$
$= \frac{1}{2}\arctan(x)x^{2} + \frac{1}{2}\arctan(x) - \int \frac{1}{2}(1)dx$
$= \frac{1}{2}\arctan(x)x^{2} + \frac{1}{2}\arctan(x) - \frac{1}{2}x$