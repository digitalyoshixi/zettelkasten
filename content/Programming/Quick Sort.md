---
tags:
  - programming
---
A [[Divide and Conquer]] [[Sorting Algorithms|Sorting Algorithm]] that is the fastest in [[Expected Analysis]].
Time complexity of:
- Worst case $\Theta(n^{2})$
- Average case $\Theta(n \log n)$
- Best case $\Theta(n \log n)$
# Algorithm
![[Quick Sort-20250317165015827.webp]]
1. Pick a pivot index at random
2. Create a sub-list for all indexes smaller than the pivot index
3. Create a sub-list for all indexes bigger than the pivot index
4. Create a sublist for the item at the pivot index
5. Recursively call this pivot algorithm
6. Base case is when the list is size of 1
# Pseudocode
```perl
quick_sort(A):
	if p < r:
		g := partition(A,g,r)
		quicksort(A,g,g-1)
		quicksort(A,g+1,r)
partition(A,p,r):
	x := A[r]
	i := p-1
	for j in p, ..., r-1:
		if A[j] <= x:
			i := i + 1
			exchange A[i] with A[j]
	exchange A[i+1] with A[r]
	return i+1
```
# Correctness Proof
Uses [[Loop Invariant]]:
- $A[k]\leq x$ for $p \leq k ,+ i$
- $A[k]> x$ for $i+1 \leq k \leq j-1$
- $A[k] = x$ for $k=r$