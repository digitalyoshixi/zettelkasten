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
	- $q_{1}, \dots,q_{n}$ being factors of $Q(x)$
	- $p_{1}, \dots p_{n}$ being functions one [[Degree]] lower than $q_{1},\dots,q_{n}$
3. Solve for the unknown constants introduced in part 2
4. Integrate
# Types of Fraction Decompositions
### Linear
This is if:
- $p_{1},\dots,p_{n}$ have degrees of 0
- $q_{1}$ has degree 1
- $q_{2}$ has degree 2
- ...
- $q_{n}$ has degree n
### Quadratic
- $p_{1},\dots,p_{n}$ have degrees of 1
- $q_{1}$ has degree 2
- $q_{2}$ has degree 4
- ...
- $q_{n}$ has degree 2n