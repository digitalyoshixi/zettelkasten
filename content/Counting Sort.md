---
tags:
  - programming
---
A [[Linear Time]] [[Stable Sorting Algorithm]] that works well for numbers less than $10$.
![[Counting Sort-20251012231447912.webp]]
# Process
1. Count all the number of occurances for each item in the array
2. Shift the counts left, so that each key points to the subsequent value
3. The value of each key indicates the index of which that value starts at.