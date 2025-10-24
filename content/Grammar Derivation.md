---
tags:
  - programming
  - math
---
A [[Non-terminal]] $\beta$ is derived by [[Non-Terminal]] $\alpha$ if there is a series of [[Production|Production Rules]] that can be applied to turn $\alpha$ into $\beta$
# Formal Definition
- Let $\alpha, \beta \in (V \cup \Sigma)^{*}$
- A derivation of $\beta$ from $\alpha$ in [[Programming/Grammar|Grammar]] $G$ is the series of strings $s_{1},\dots,s_{n}$  where:
	- $s_{1} = \alpha$ 
	- $s_{n} = \beta$
	- $s_{i} \Rightarrow_{G} s_{i+1}$ (Each string has a [[Production]] to the next one)
