---
tags:
  - programming
  - math
aliases:
  - Derivation
---
The set of [[Production|Production Rules]] that can be applied to [[Non-terminal]] $\alpha$ into [[Non-terminal]] $\beta$.
- Can be thought of as a path in a [[Parse Tree]]
# Formal Definition
- Let $\alpha, \beta \in (V \cup \Sigma)^{*}$
- A derivation of $\beta$ from $\alpha$ in [[Programming/Grammar|Grammar]] $G$ is the series of strings $s_{1},\dots,s_{n}$  where:
	- $s_{1} = \alpha$ 
	- $s_{n} = \beta$
	- $s_{i} \Rightarrow_{G} s_{i+1}$ (Each string has a [[Production]] to the next one)
