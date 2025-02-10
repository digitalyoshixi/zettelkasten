---
tags:
  - math
  - calculus
---
An [[Integral Solving Techniques|Integration Technique]] used to rewrite [[Proper Rational Function|Proper Rational Functions]] into equivalent partial fractions.
# Process
Given a [[Proper Rational Function]] in the form $f(x)=\frac{P(x)}{Q(x)}$
1. Factor $Q(x)$ into irreducible factors
2. Write the fraction decomposition in the form of a [[Quotient Functions|Quotient Function]] sum: $$f(x) = \frac{p_{1}(x)}{q_{1}(x)} + \dots + \frac{p_{n}(x)}{q_{n}(x)}$$ with:
	- $q_{1}, \dots,q_{n}$ adhering to rule 1 or rule 2 of the irreducible factors of $Q(x)$
	- $p_{1}, \dots p_{n}$ being functions one [[Degree]] lower than its respective $q_{1},\dots,q_{n}$
3. Solve for the unknown constants introduced in part 2
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
# Example
Convert $f(x) = \frac{x^{2} + \pi}{(x^{2} + 1)^{2}(x^{4})(2x-7)}$ into a partial fraction decomposition.
5. The irreducible denominator factors are: $(x^{2}+1), x, 2x-7$
6. Then, the list of $q$ functions are: $x^{2}+1, (x^{2}+1)^{2}, x, x^{2}, x^{3}, x^{4}, 2x-7$. We make:
$$f(x) = \frac{Ax+G}{x^{2}+1} + \frac{Bx+H}{(x^{2}+1)^{2}} + \frac{C}{x} + \frac{D}{x^{2}} + \frac{E}{x^{3}} + \frac{F}{x^{4}} + \frac{I}{2x-7}$$
by rule 1 and rule 2.
