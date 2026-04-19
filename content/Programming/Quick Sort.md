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
quick_sort(A, low, high):
	# takes entire list or sublist and recursively sorts it with partition
	if low < high:
		pivot := partition(A,low,high)
		quicksort(A,low,pivot-1)
		quicksort(A,pivot+1,high)

partition(A, low, high):
	# takes the subarray, the start of array with low, end of array with high, swaps based off a pivot which is last element and returns pivot index
	x := A[high]
	i := low-1 # i indicates end of smaller partition
	j := low # j indicates end of higher partition
	while j < high:
		if A[j] <= x:
			i := i + 1
			exchange A[i] with A[j]
		j++
	exchange A[i+1] with A[x]
	return i+1 # returns the pivot's final index
```
# Correctness Proof
Uses [[Loop Invariant]]:
- $A[k]\leq x$ for $p \leq k ,+ i$
- $A[k]> x$ for $i+1 \leq k \leq j-1$
- $A[k] = x$ for $k=r$