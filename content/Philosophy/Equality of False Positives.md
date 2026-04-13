---
tags:
  - philosophy
---
Members of groups should have the same chance to be classified negatively.
[[False Positive]] rate should be the same across all relevant groups.
The algorithm fails for each group the same way.
# Issues
- Hard to implement as an algorithm, because you must assume the false positive rate for each group first.
- No [[Ex-post Fairness]], concerned with [[Ex-ante Fairness]]
![[Equality of False Positives-20260413031543876.webp]]
- In this case, the optimal threshold for acceptance will accept all circle students as it would be the case that any student below the threshold meets the % required for false positive in each group. This would incorrectly reject 5 square students that could have succeeded. 
- For groups with different sizes, certain cases can have a disproportionate high false rejection rate, fails [[Equality of False Negatives]]