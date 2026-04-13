---
tags:
  - math
  - statistics
aliases:
  - Impossibility Theorem
---
Some metrics aren't compatible with other metrics of fairness.
- Predictive accuracy of the best college students from SAT scores (yields to priviledged class)
# Theorem
[[Predictive Parity]] and [[Classification Parity]] are not equal accuracy
Alternatively, [[Calibration]] and [[Statistical Parity by Status]] are in tension.
# Results
- [[Calibration Within Groups|CWG]], [[Balance for the Positive Class]], [[Balance for the Negative Class]] cannot be satisfied all together unless base rates are equal across groups, or the algorithm is perfect
- [[Equality of False Positives]], [[Equality of False Negatives]], [[Equality of Positive Predicated Value|PPV]] cannot be satisfied all together
- No algorithm can satisfy more than one of
	- [[Equality of False Positives]] and [[Equality of False Negatives]]
	- [[Equality of Positive Predicated Value|PPV]] and [[Equality of Negative Predictive Value]]
	- [[Equal Ratios of Predicted Positives to Actual Positives]]
- No algorithm can satisfy both [[Equal Overall Error Rates]] and [[Proportionality|Statistical Parity]] unless base rates are equal across groups
- No algorithm can satisfy [[Equal Ratios of False-Positive Rate to False-Negative Rate]] and [[Proportionality|Statistical Parity]] unless base rates are equal or no group has [[False Positive]] or [[False Negative]]
# Proof
https://www.marcellodibello.com/algorithmicfairness/handout/impossibility.html