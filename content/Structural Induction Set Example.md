---
tags:
  - math
  - programming
---
# Example
With a well-formed set of expressions comprised of:
- Variables $x,y,z,\dots$
- Operations $+,-, \times, \dots$
Define the [[Alphabet]] for the expressions $\{ x,y,z,+,-,x,\div, (, ) \}$
Let $\mathcal{E}$ be the smallest set.
##### Base Case
Let our base case be $x,y,z \in \mathcal{E}$
##### Induction Step
Assume $e_{1}, e_{2} \in \mathcal{E}$ then, $(e_{1}+e_{2}), (e_{1} - e_{2}), (e_{1} \times e_{2}), (e_{1} \div e_{2}) \in \mathcal{E}$
...