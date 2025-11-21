---
tags:
  - math
  - proofs
aliases:
  - Existential Quantifier
---
A [[Quantifier]].
$$\exists$$
There exists atleast one.
It is applied immediately to the free variable after, $\exists x$,  rather than for the entire statement similar to how $\neg$ is only for a single term after
# Existentially Quantified
$\exists x, P(x)$
- True if P(x) is true for some element in the [[Universal Domain|Universe of Discourse]]
- False otherwise
# Quantifier Negation Laws
$$\neg \forall,P(x) \equiv \exists x, \neg P(x)$$  $$\neg \exists, P(x) \equiv \forall x,\neg P(X)$$ Negate the predecates, and the quantifier
### Negating Predicates with Negated Quantifiers
$$\exists x\neg \forall y, C(y,x)$$
1. Remove all negations in front of quantifiers
2. Flip quantifiers
# Proof Writing
$\exists x \in D$ such that $D(x)$
Choose x = __ (this could be a variable or concrete value) then prove both $x \in D$ and $P(x)$ is true.
# Unique Existence
- [[Unique Existence]]