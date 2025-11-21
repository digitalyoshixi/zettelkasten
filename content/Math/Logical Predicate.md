---
tags:
  - math
  - discrete_math
aliases:
  - Predicate
---
A [[Mathematical Statement]] $P$ about a variable $x$.

These are translations from English sentences to logical statements that take an arbitrary [[Free Variable]] like P(x). The quantifiers can be evaluated with an input to return true or false
They tend to paired with [[Logical Connectives]] and [[Logical Predicate]]
# Definitions
### [[Function]] Definition
With a non-empty [[Domain]]:
A predicate is a function $A : D^{n} \to \{ 0,1 \}$ with [[Arity]] $n$
$$A(x_{1},\dots,x_{n}) = \begin{cases}
1 \text{ if } (x_{1},\dots,x_{n}) \in A\\ \\
0 \text{ otherwise}
\end{cases}$$ 
(Like an [[Indicator Random Variable|Indicator RV]])
### [[Relation]] Definition
With a non-empty [[Domain]]:
A predicate is the [[Relation]] $A \subset D^{n}$
$$A = \{ (x_{1},\dots,x_{n}) \in D_{n} | A(x_{1},\dots,x_{n})=1 \}$$
# Example Predicates
$P(n) : n^{2} = n$
Assumed by default to apply to all $n$. Don't add any [[Quantifier|Quantifiers]] in the definition.
# Types
- [[For All|Universal Quantifier]]
- [[There Exists|Existential Quantifier]]
- [[Bound Quantifier]]
# Laws
- [[Quantifier Negation Laws]]