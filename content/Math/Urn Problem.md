---
tags:
  - math
  - statistics
---
# Problem
- We have $N$ balls in total
- $m$ balls are white
- $N - m$ balls are black
- We pick $n$ balls without replacement
# Proposed Solution
A [[Hypergeometric Distribution]] with [[Random Variable|RV]] $X$ to denote the # of white balls out of $n$ balls chosen.
# Example
- With $N = 10$
- With $m = 7$
- With $N - m = 3$
- With $n = 5$
Then,
- $x = 2,3,4,5$
- In general, $P(X = x) = \frac{\binom{m}{x} \binom{N-m}{n-x}}{\binom{N}{n}}$