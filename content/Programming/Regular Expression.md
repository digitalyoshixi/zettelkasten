---
tags:
  - programming
  - linguistics
aliases:
  - Regex
---
These are [[String|Strings]] used to define search patterns of strings.
The alphabet includes: $\mathcal{RE} = \{ \emptyset, \epsilon, +, *, (, )  \}$. Assumes the alphabet you match does not include any of these symbols.
# Notations
- $\epsilon$ - empty string representing empty set $\emptyset$ or $\{ \epsilon \}$
- any symbol '$a$' from the input alphabet representing $\{ a \}$
- Union $(a + b)$ representing $\{ a,b \}$
- Concatenation $(ab)$ which is valid if and only if $a,b$ 
- [[Kleene Star]] $(a)^{*}$ zero or more occurrences of $a$