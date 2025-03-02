---
tags:
  - math
  - calculus
aliases:
  - PFD
---
An [[Integral Solving Techniques|Integration Technique]] used to rewrite [[Proper Rational Function|Proper Rational Functions]] into equivalent partial fractions.
# Process
Given a [[Proper Rational Function]] in the form $f(x)=\frac{P(x)}{Q(x)}$
1. Factor $Q(x)$ into irreducible factors
2. Write the fraction decomposition in the form of a [[Quotient Functions|Quotient Function]] sum: $$f(x) = \frac{p_{1}(x)}{q_{1}(x)} + \dots + \frac{p_{n}(x)}{q_{n}(x)}$$ with:
	- $q_{1}, \dots,q_{n}$ adhering to rule 1 or rule 2 of the irreducible factors of $Q(x)$
	- $p_{1}, \dots p_{n}$ being functions one [[Degree]] lower than its respective $q_{1},\dots,q_{n}$
3. Solve for the unknown constants introduced in part 2 by:
	1. Equating $P(x) = \frac{p_{1}(x)Q(x)}{q_{1}(x)} +\dots+ \frac{p_{n}(x)Q(x)}{q_{n}(x)}$
	2. Factoring $P(x)$, then finding what values of $p(x)$ allow $P(x)$ to be 0
4. Integrate
# Fraction Decomposition Rules
### Linear (Rule 1)
This is if:
- $p_{1},\dots,p_{n}$ have degrees of 0
- $q_{1}$ has degree 1
- $q_{2}$ has degree 2
- ...
- $q_{n}$ has degree n
### Quadratic (Rule 2)
- $p_{1},\dots,p_{n}$ have degrees of 1
- $q_{1}$ has degree 2
- $q_{2}$ has degree 4
- ...
- $q_{n}$ has degree 2n
# Examples
### Example 1
Find the integral of: $$\int \frac{1}{(x+2)(x-2)}\, dx$$
1. We can represent the decomposition as: $$\int \frac{A}{x+2}dx + \int \frac{B}{x-2}dx $$
2. Solving for constants: $$1 = A(x-2) + B(x+2)$$
3. With $x=2 \implies 1=A(0)+B(4) \implies B = \frac{1}{4}$
4. With $x=-2 \implies 1 = A(-4)+B(0) \implies A = -\frac{1}{4}$
5. Thus, $$=\int \frac{-\frac{1}{4}}{x+2}dx + \int \frac{\frac{1}{4}}{x-2}dx $$
6. $$= -\frac{1}{4}\int \frac{1}{x+2} dx + \frac{1}{4}\int \frac{1}{x-2} dx$$
7. $$= -\frac{1}{4}\ln|x+2| + c+\frac{1}{4}\ln|x-2| +c$$
8. $$= \frac{1}{4}\ln \frac{|x-2| }{|x+2|} +c$$

### Example 3
Find the integral of: $$\int \frac{x}{(x-1)(x-2)^{2}}\, dx$$
1. We can represent the decomposition as: $$\int \frac{A}{x-1}dx + \int \frac{B}{x-2}dx + \int \frac{C}{(x-2)^{2}} dx$$
2. Then, $x = A(x-2)^{2} + B(x-2)(x-1)+C(x-1)$
3. $x=2 \implies C =  2$
4. $x=1 \implies A =  1$
5. $x=3 \implies B = -1$
6. Then, $$=\ln(\frac{|x-1|}{|x-2|}) - \frac{2}{x-2}+c$$
Note we used [[Integration by Substitution]] for this one aswell.
