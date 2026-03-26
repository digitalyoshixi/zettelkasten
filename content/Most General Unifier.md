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