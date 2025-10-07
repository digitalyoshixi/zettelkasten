---
tags:
  - programming
  - math
aliases:
  - Regex Matches
---
# Definition
- Let $R$ be a regex
- $\mathcal{L}(R)$ is the set of [[String|Strings]] in [[Full Language]] $\Sigma^{*}$ that match $R$
# Matches
- $\mathcal{L}(\emptyset) = \emptyset$
- $\mathcal{L}(\epsilon) = \{ \epsilon \}$
- $\mathcal{L}(c) = \{  c \}$, $\forall c \in \Sigma$
- $\mathcal{L}( (S+T) ) = \mathcal{L}(S) \cup \mathcal{L}(T)$
- $\mathcal{L}( (ST) ) = \mathcal{L}(S)\mathcal{L}(T)$
- $\mathcal{L}(S^{*}) = \mathcal{L}(S)^{*}$