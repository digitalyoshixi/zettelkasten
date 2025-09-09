---
tags:
  - statistics
aliases:
  - Bayes Rule
---
# Theorem
$$
P(A|B) = P(A) \times \frac{P(B|A)}{P(B)}
$$
# Robust Version
$$
P(A_{j}|B) = \frac{P(B|A_{j})P(A_{j})}{ \sum_{i=1}^{n} P(B|A_{i})P(A_{i})}
$$
### Single Partition
$$
P(A|B) = \frac{P(B|A)P(A)}{P(B|A)P(A) + P(B|A^{c})P(A^{c})}
$$