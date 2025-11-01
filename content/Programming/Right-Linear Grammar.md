---
tags:
  - programming
  - math
---
A restricted [[Context Free Grammar|CFG]] where every [[Production]] is either the empty string or a string of terminals followed by a variable.
# Definition
A [[Context Free Grammar|CFG]] $G = (V, \Sigma, P, S)$ is right linear if:
- Every production $P$ is of the form:
	- $A \to \epsilon$
	- $A> xB$, $A,B \in V, x \in \Sigma^{*}$
# Types
- [[Strict Right Linear Grammar]]