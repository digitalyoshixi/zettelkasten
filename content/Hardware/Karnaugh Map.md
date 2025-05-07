---
tags:
  - hardware
  - electricity
aliases:
  - K-Map
---
Used for simplifying digital circuits with 3-4 varaibles.
# Forms
- [[Sum of Product K-Map]]
- [[Product of Sum K-Map]]
# Steps to Solve
1. Find min-terms, max-terms
2. Select K-map according to number of variables
	1. For SOP, put 1's in blocks of K-map respective to minterms, and (0's elsewhere)
	2. For POS, put 0's in blocks of K-map repective to max terms (1's elsewhere)
3. Make rectangular groups containing total terms in powers of 2,4,8 (except 1)
	1. For SOP, find the product terms and sum them up for SOP form