---
tags:
  - programming
  - linguistics
aliases:
  - Regex
---
These are [[String|Strings]] used to define search patterns of strings.
# Notations
- $\epsilon$ - empty string representing empty set $\emptyset$ or $\{ \epsilon \}$
- any symbol '$a$' from the input alphabet representing $\{ a \}$
- Union $(a + b)$ representing $\{ a,b \}$
- Concatenation $(ab)$ which is valid if and only if $a,b$ 
- [[Kleene Star]] $(a)^{*}$ zero or more occurrences of $a$
# Alphabet Definition
The alphabet includes: $\mathcal{RE} = \{ \emptyset, \epsilon, +, *, (, )  \}$. Assumes the alphabet you match does not include any of these symbols.
# Definition
Define the set of regexes of $\Sigma$
Let $\mathcal{RE}$ be the smallest set such that:
Basis: $\emptyset, \epsilon \in \mathcal{RE}, c \in \mathcal{RE}, \forall c \in \Sigma$
- Note that $\emptyset$ is a symbol, not the set
- Note that $\epsilon$ is a symbol, not the string
Induction step: if $S,T \in \mathcal{RE}$, then $(S+T), (ST), S^{*} \in \mathcal{RE}$
# Concepts
- [[Semantics of Regular Expressions|Regex Matches]]
- [[Regex Precedences]]