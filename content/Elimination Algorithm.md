---
tags:
  - math
  - linalg
---
Input: An $n \times k$ matrix ($M \in M_{n \times k}(\mathbb{F})$)
Output: A matrix $M'$ in [[Echelon Form]] equivalent to $M$
# Process
1. Check for zero rows. If the rows $R_{r}$ for $i \leq r\leq n$ are all zeroes, then we're done
2. Otherwise, find the first non-zero coeff. find the $a_{rj} \neq 0$ with the smallest $j$ and $r \geq i$
	1. Divide out $a_{rj}$ by applying the operation $M \xrightarrow{\frac{1}{a_{rk}}R_{r}}M_{next}$
	2. Exchange $R_{i}$ and $R_{r}$ by applying operation $M \xrightarrow{R_{r} \leftrightarrow R_{i}}M_{next}$
	3. Clear the column $j$th column using operation $M \xrightarrow{-a_{rj}R_{i}+R_{j}}M_{next}$
3. Run the elimination algorithm on $M_{next}$

This process is based off the [[Every Linear System Has A Row-Echelon Form Theorem]]