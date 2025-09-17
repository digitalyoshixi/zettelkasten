---
tags:
  - statistics
  - probability
aliases:
  - Proving Conditional Independence
---
# Example
Given a fair coin $(H/T)$
Given a biased coin $(H/H)$
If we pick one and flip twice, are the flip results independent?
### Soln
With events $H_{1}$ and $H_{2}$ being flipping heads on the first flip and heads on the second flip.
The events are independent if: $P(H_{1} \cap H_{2}) = P(H_{1})P(H_{2})$
- Note that $P(H_{1} \cap H_{2}|F) = P(H_{1}|F) \times P(H_{2}|F) = \frac{1}{4}$ given a fair coin is chosen
- Note that $P(H_{1} \cap H_{2}|B) = P(H_{1}|B) \times P(H_{2}|B) = 1$ given a biased coin is chosen
Then, we have shown that the two events have [[Conditional Independence]]
Then, consider $P(H_{1} \cap H_{2}) = P(H_{1} \cap H_{2} \cap B) + P(H_{1} \cap H_{2} \cap F)$
- $\implies P(H_{1} \cap H_{2}) = P(H_{1} \cap H_{2}|B)*P(B) + P(H_{1} \cap H_{2} | F) * P(F)$
- $\implies P(H_{1} \cap H_{2}) = \frac{5}{8}$
Then, consider $P(H_{1}) = P(H_{1} | B)P(B) + P(H_{1} |F)P(F)$
- $\implies P(H_{1}) = \frac{3}{4}$
Similarly, we compute $P(H_{2}) = \frac{3}{4}$

Then, since $\frac{5}{8} \neq \frac{3}{4} * \frac{3}{4}$ the two are not independent