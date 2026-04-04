---
tags:
  - programming
aliases:
  - Amortized Analysis
---
A given method to analyze complexity of an algorithm by looking at resource usage on average.
Amortized time is the total amortized cost divided by all operations performed.
Gives a tighter bound than worse case analysis.
![[Amortized Time-20260404213259172.webp]]
# Definition
If $n$ operations take a total of $O(f(n))$ total time in worst case, then each operation takes $O\left( \frac{f(n)}{n} \right)$ amortized time.
# Methods
- [[Amortized Aggregate Method]]
- [[Amortized Accounting Method]]
- [[Amortized Potential Method]]