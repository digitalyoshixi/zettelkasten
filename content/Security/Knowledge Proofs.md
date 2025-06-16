---
tags:
  - information_theory
  - security
---
You know something, if when given an input that includes [[Knowledge]], you can efficiently extract the knowledge from that input.
# Definition
1. With $R,X,W$ as [[Efficiently Recognizable Language|Efficiently Recognizable Languages]]
2. With $R \subset X \times W$
3. With $X$ as the set of statements
4. With $W$ as the set of witnesses
5. We say $x \in X$ is true if $\exists w \in W, (x,w) \in R$. Otherwise, it is false
6. We call $R$ an [[Effective Relation]]
### Intuition
- For all possibly cheating [[Cryptographic Protocol|Protocols]] $\hat{P}$ that make $V$ output *accept*, we can efficiently **extract** a [[Zero Knowledge|Witness]] from $\hat{P}$ by rewinding it.
# Example
- [[Discrete Logarithm Language]]