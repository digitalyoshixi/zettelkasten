---
tags:
  - math
  - discrete_math
---
A [[Mathematical Statement]] $P$ about a variable $x$
These are translations from English sentences to logical statements that take an arbitrary [[Free Variable]] like P(x). The quantifiers can be evaluated with an input to return true or false
They tend to paired with [[Logical Connectives]] and [[Logical Predicate]]:
# Defining Predicates
$P(n) : n^{2} = n$
Assumed by default to apply to all $n$. Don't add any [[Quantifier|Quantifiers]] in the definition.
# Universal Quantified
For a statement $P(x)$:
$\forall x, P(x)$
- True if P(x) is true for every element in the [[Universal Domain|Universe of Discourse]]
- False otherwise
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
3. 
# Bound Quantifiers
This is when the [[Universal Domain|Universe of Discourse]] is bounded
$\forall x \in A,P(x)$ is short for $\forall x,x \in A \implies P(x)$
$\exists x \in A, P(x)$ is short for $\exists x, x \in A \wedge P(x)$
### Bound Quantifiers When $A = \emptyset$
If $A$ is the empty set $\emptyset$ then,
$\forall x \in \emptyset, P(x)$ is [[Vacuously True]]
$\exists x \in \emptyset,P(x)$ is False
# Quantifier Abbreviation
$\forall x(x \in A \to P(x)) \equiv \forall x \in A \ P(x)$