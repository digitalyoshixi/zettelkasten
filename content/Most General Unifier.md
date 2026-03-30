---
tags:
  - programming
  - prolog
aliases:
  - MGU
---
Many [[Propositional Formula|Formula]] have multiple [[Unifier]]. We can describe all of them in a general way.
# Example
For atomic formulas $p(X,f(Y))$ and $p(g(U), V)$:
- Unifier A: $\{ X / g(a), Y/b, U / a, V/f(b) \}$ to $p(g(a),f(b))$
- Unifier B: $\{ X / g(c), Y / d, U / c, V / f(d) \}$ to $p(g(c), f(d))$
MGU of two atomic formulas to give $p(g(U), f(Y))$
# Example 2
Lets generalize these unifiers:
- $f(W,g(Z), Z)$
- $f(X,Y,h(X))$
First:
- $W = X$
- $g(Z) = Y$
- $Z = h(X)$
Then, lets substitute
- $Z = h(W)$
- $Y = g(h(W))$
Then, final one is:
$f(W, g(h(W)), h(W))$
# Generality
- The MGU is most general, because all other unifiers are too specific
- A substitution $\sigma$ is most general of a set of expressions $E$ if it unifies $E$ and for any unifier $w$ of $E$, there is a unifier $\lambda$ s.t $w = a \circ \lambda$