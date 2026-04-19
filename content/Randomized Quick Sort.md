---
tags:
  - programming
---
A revised [[Quick Sort]] algorithm that uses [[Sampling Techniques|Random Sampling]].
# Pseudocode
```perl
r_quicksort(A,p,r):
	if p < r:
		g = r_partition(A,p,r)
		r_quicksort(A,p,g-1)
		r_quicksort(A,g+1,p)
		
r_partition(A,p,r):
	exchange A[r] with A[random(p,r)]
	x := A[r]
	i := p-q
	for j in p, ..., r-1:
		if A[j] <= x:
			i := i + 1
			exchange A[i] with A[j]
	exchange A[i+1] with A[r]
	return 1+1
```
# Complexity Analysis
- Quicksort is $O(n+X)$ where:
	- $n$ is length of array $A$
	- $X$ is total number of elements smaller than the random pivot
- Random quicksort expected time is: $E(X) = E( \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} X_{ij})$
- $= \sum_{i=1}^{n-1} \sum_{j=i+1}^{n}Pr(z_{i} \text{ is compared to }z_{j})$
- $= Pr(z_{i} \text{ or } z_{j} \text{ is the first pivot chosen from } Z_{ij})$
- $= \frac{2}{j-i+1}$
- $\implies E(x) = 2(n-1)\ln(n) \in O(n\log n)$