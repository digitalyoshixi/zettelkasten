---
tags:
  - programming
---
A method to collect [[Amortized Time]].
# Method
1. Sum the [[Time Complexity|Worst Case Costs]] for each operation
2. Examine if any operations depend on each other and simplify
3. Divide total cost by # of operations
# Example
Data structure where the $i$-th operation costs $i$ if it is an exact power of 2, $1$ otherwise.
Find aggregate cost per operation.
Soln:
$$
c_{i} = \begin{cases}
i & \text{ if } i \text{ exact power of 2} \\
1 & \text{ o/w}
\end{cases}
$$
- $\sum_{i=1}^{n}c_{i} \leq n + \sum_{j=1}^{\log n}2^{i} <n+2^{\log(2n)}=n+2n=3n$
- Then, aggregate cost is $\frac{3n}{n} = 3$
