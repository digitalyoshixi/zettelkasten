---
tags:
  - math
  - linalg
---
Input: An $n \times k$ matrix ($M \in M_{n \times k}(\mathbb{F})$)
Output: A matrix $M'$ in [[Echelon Form]] equivalent to $M$
# Process
1. Check for zero rows. If the rows $R_{r}$ for $i \leq r\leq n$ are all zeroes, then we're done
2. Divide out $a_{rj}$ by applying the operation $M \xrightarrow{\frac{1}{a_{rk}}}$