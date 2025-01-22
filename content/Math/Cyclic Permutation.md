---
tags:
  - math
  - discrete_math
---
If a sequence repeats itself, and you want to see the number of unique permutations there are then the formula is:
# Rotation Symmetry
$$(n-1)!$$
# Mirror Symmetry
$\frac{(n-1)!}{2}$
# Intuition
Suppose you have a table with 4 seats and 4 people to be seated.
![[Cyclic Permutation-20241205153240666.webp|284]]
The possible seating arrangements before dedup is $_{4}P_{4} = 4!$
![[Cyclic Permutation-20241205153325050.webp|272]]
To remove all the duplicates, think about the # of times it could be shuffled around and still have the same order (person to the left is still to the left after a shuffle)
![[Cyclic Permutation-20241205153526933.webp]]
So, divide by 4 and you get $\frac{4!}{4} = 3! = (4-1)!$
