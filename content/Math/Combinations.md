---
tags:
  - math
aliases:
  - Binomial Coefficient
---
 $_n$C$_r$ or C(n,r) or (n/r).
A selection from a group of items without regard to order
# Combinations Formula
$_{n}C_{r} = \frac{_{n}P_{r}}{r!}$
 = $\frac{n!}{(n-r)!(r!)}$
# Concepts
- [[Combination Subset Formula]]
- [[Combinations with Repetition]]
- [[Divisors with Combinations]]
- [[Hockey Stick Identity]]
- [[Problem Solving with Combinations]]
# Examples
## Example 1
in how many ways can: A, B, C, D and E, create a comittee?
5 People, 3 boxes
![[Pasted image 20230926141928.png]]
The order doesn't matter. they are the same comittee.
To find this, you find the permutations, then divide by the permutations the boxes can have.
1. Permutations: $_5$P$_3$ = 60
2. Duplicate boxes = 3! = 6. Example: 
![[Pasted image 20230926142153.png]]
3. 60/6 = 10
## Example 2
How many different sampler dishes can you have with 3 different flavors could you get in an ice cream shop with 31 different flavors? doesn't matter what order the flavors are in.
```
n = 31
r = 3
31!/(28!)(3!)
= 4495
```