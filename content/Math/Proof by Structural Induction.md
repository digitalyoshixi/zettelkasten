---
tags:
  - proofs
  - math
---
Proof method used widely in [[Graph Theory]].
Used to prove some [[Logical Predicate]] $P(x)$ holds for all $x$ of some [[Inductive Definition|Recursively Defined Data Structure]]
# Process
1. Define $P(x)$
##### Base Case
1. For axiom 1
	1. Prove $P(x)$
2. For axiom 2
	1. Prove $P(x)$
##### Induction Step
1. Suppose $P(x)$ holds for sub-structures used in recursive step of definition
	1. Prove $P$ holds for the recursively constructed structure
# [[Regular Expression|Regex]] Structure
1. Define $P(x)$ to be that a given regex is in $\mathcal{RE}$
##### Base Case
- Suppose $\emptyset, \epsilon$, single letter $a$ are in $\mathcal{RE}$
- Show $P(\emptyset), P(\epsilon), P(a)$
##### Inductive Step
If regexes $S$ and $T$ are in $\mathcal{RE}$, then show:
- $P(S),P(T) \implies P(S+T)$
- $P(S),P(T) \implies P(ST)$
- $P(S),P(T) \implies P(S^{*})$
# Examples
- [[Structural Induction Set Example]]
- [[Structural Induction String Example]]
- [[Structural Induction Regular Expression Example]]
- [[Proving Set is Complete]]
- [[Set of First Order Predicate Formula]]