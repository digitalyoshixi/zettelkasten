---
tags:
  - programming
---
A given method to analyze complexity of an algorithm by looking at resource usage on average.
Amortized time is the total amortized cost divided by all operations performed.
# Definition
If $n$ operations take a total of $O(f(n))$ total time in worst case, then each operation takes $O\left( \frac{f(n)}{n} \right)$ amortized time.
# Methods
- [[Amortized Aggregate Method]]
- [[Amortized Accounting Method]]
- [[Amortized Potential Function]]