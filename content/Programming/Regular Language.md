---
tags:
  - programming
---
These are [[Programming/Language|Languages]] that can be created from a [[Regular Expression|Regex]].
# Formal Definition
$L = \mathcal{L}(R)$ for a given regex $R$
Where $\mathcal{L}(\cdot)$ is the [[Language of Regex]]
# Language Properties
- $\mathcal{L}(\emptyset) = \emptyset$
- $\mathcal{L}(\epsilon) = \{ \epsilon \}$
- $\mathcal{L}(c) = \{  c \}$, $\forall c \in \Sigma$
- $\mathcal{L}( (S+T) ) = \mathcal{L}(S) \cup \mathcal{L}(T)$
- $\mathcal{L}( (ST) ) = \mathcal{L}(S)\mathcal{L}(T)$
- $\mathcal{L}(S^{*}) = \mathcal{L}(S)^{*}$
# Concepts
- [[Regular Expression|Regex]]
- [[Closure of Regular Expressions]]