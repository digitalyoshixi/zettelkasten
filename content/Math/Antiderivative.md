---
tags:
  - calculus
---
A function $F$ is an antiderivative $f$ on an interval $l$ if $F'(x) = f(x)$ for all $x$ in $l$
For example, position is the antiderivative of velocity.
# Infinite Antiderivatives
If you want to find the antiderivative of a given $F$, you can create infinite $f$ functions.
### Example
$v(t) = d'(t)$
$v(t) = t^2$
$d(t)$ could be $\frac{1}{3}t^3 + 0, \frac{1}{3}t^3 + 1 , \frac{1}{3}t^3 + 2, \dots$ 
### Process
![[Antiderivative-20240801024436411.webp|484]]
1. Increase power by 1 for each term
2. New coefficients are old coefficients divided by new power
3. Add constant $c$
# Particular Antiderivative Table

| $f(x)$            | General $F(x)$           |
| ----------------- | ------------------------ |
| $1$               | $x$                      |
| $x^n$             | $(\frac{1}{n+1})x^{n+1}$ |
| $\frac{1}{1+x^2}$ | $\tan^{-1}(x)$           |
# Anti derivative Proofs
- [[Proving f'(0) has f as constant function]]
	- [[Proving Antiderivative is g(x) + c]]