---
tags:
  - probability
  - statistics
aliases:
  - LoTP
---
![[Law of Total Probability-20250902135628540.webp]]
# Law
- $\forall$ [[Partition]] $A_{1} ,A_{2} \dots$
- For arbitrary event $B$
- $P(B) = P(B \cap S)= \sum_{i=1}^{n}P(B \cap A_{i})$
### Generalization
$P(A) = P(A \cap B) + P(A \cap B^{c})$
# Proof
1. Note that $P(B \cap S) = \sum_{i=1}^{n}P(B \cap A_{i})$
2. Then, the sample space is also $S = \cup_{i} A_{i}$ by defn [[Disjoint]]
3. Then, $P(B \cap S) = P(B \cap (\cup_{i}A_{i})) = P(\cup_{i}(B \cap A_{i}))$
4. Note that $B \cap A_{i}$ are also [[Disjoint]]
5. Then, using the third [[Probability Axioms|Probability Axiom]], $P(\cup_{i}(B \cap A_{i})) = \sum_{i=1}^{n} P(B \cap A_{i})$
### Intuition
The probability of a event intersecting the sample space is the sum of probability of the intersection of each disjoint.
