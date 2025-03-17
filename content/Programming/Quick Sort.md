---
tags:
  - programming
---
A [[Sorting Algorithms|Sorting Algorithm]] that is the fastest in all cases.
Time complexity of:
- Worst case $O(n^{2})$
- Best case $O(\log_{2}n)$
# Algorithm
![[Quick Sort-20250317165015827.webp]]
1. Pick a pivot index at random
2. Create a sub-list for all indexes smaller than the pivot index
3. Create a sub-list for all indexes bigger than the pivot index
4. Create a sublist for the item at the pivot index
5. Recursively call this pivot algorithm
6. Base case is when the list is size of 1
