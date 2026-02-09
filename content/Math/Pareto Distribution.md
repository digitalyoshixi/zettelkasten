---
tags:
  - politics
  - law
  - statistics
---
A distribution indicating a survival function.
Can be used to model:
- Tradeoffs between [[Fairness]] and [[Model Accuracy]]
# PDF
$$
\frac{\alpha x^{\alpha}_{m}}{x^{\alpha+1}}
$$
# CDF
$$
F_{X}(x) = \begin{cases}
1 - \left( \frac{x_{m}}{x} \right)^{\alpha} & x > x_{m}, \\
0 & x < x_{m}
\end{cases}
$$
