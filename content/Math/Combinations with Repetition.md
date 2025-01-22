---
tags:
  - math
  - discrete_math
aliases:
  - Stars and Bars
---
$$_{n+r-1}C_{r}$$
or
$$_{n+r-1}C_{n-1}$$
or
$$\frac{(r+n-1)!}{r!(n-1)!}$$
# Intuition
![[Combinations with Repetition-20241205163829076.webp]]
Best visualized if you think of the item pool being selected like:
![[Combinations with Repetition-20241205163929521.webp]]
Where:
- Elements are arranged left to right in the boxes starting from element id 1 to element id n
- Bars tell us when to stop placing our current element and move onto the next element
Note that there can be at most $r-1$ bars as you cannot have a partition with no category.
Then, if we add these bars into our element pool, you get:
![[Combinations with Repetition-20241205164145072.webp|706]]
Then the combinations are:
$_{n+r-1}C_{r}$
# Stars and Bars for Sums Of Numbers
$$_{\text{sum+\#divisors}-1}C_{{\text{\#divisors}-1}}$$
Used to find the number of solutions to an equation.
# Example
If for example you have $x_{1} +x_{2} + x_{3} + x_{4} = n$,
to find all possible solutions you can do:
$$_{n_{1}+4-1}C_{3}$$