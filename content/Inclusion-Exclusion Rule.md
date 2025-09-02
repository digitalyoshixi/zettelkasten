---
tags:
  - probability
  - statistics
---
![[Inclusion-Exclusion Rule-20250902140257052.webp]]
# Rule
### Two Events
- For any two events $A$, $B$
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
### Generalized Events
- For $n$ events $A_{1},\dots,A_{n}$
- $P(\cup_{i=1}^{n}A_{i}) = \sum_{i=1}^{n}P(A_{i}) - \sum_{j=1}^{i}P(A_{i} \cap A_{j}) + \sum_{k=1}^{j} P(A_{1} \cap A_{j} \cap A_{k})$
- $\implies P(\cup_{i=1}^{n}A_{i}) = (-1)^{n-1}P(A_{1} \cap \dots \cap A_{n})$
