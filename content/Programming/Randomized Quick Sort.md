---
tags:
  - programming
---
A revised [[Quick Sort]] algorithm that uses [[Sampling Techniques|Random Sampling]] to pick the pivot value (not always the final element of sublist).
# Complexity Analysis
- Quicksort is $O(n+X)$ where:
	- $n$ is length of array $A$
	- $X$ is total number of elements smaller than the random pivot
- Random quicksort expected time is: $E(X) = E( \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} X_{ij})$
- $= \sum_{i=1}^{n-1} \sum_{j=i+1}^{n}Pr(z_{i} \text{ is compared to }z_{j})$
- $= Pr(z_{i} \text{ or } z_{j} \text{ is the first pivot chosen from } Z_{ij})$
- $= \frac{2}{j-i+1}$
- $\implies E(x) = 2(n-1)\ln(n) \in O(n\log n)$