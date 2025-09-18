---
tags:
  - math
aliases:
  - Binomial Coefficient
---
A unordered collection of $k$ objects without repetition from $n$ possible objects.
It is a selection from a group of items without regard to order.
# Notation
 - $_nC_r$
 - $C(n,r)$
 - $C_{n}^{r}$
 - $\binom{n}{r}$
# Combinations Formula
$_{n}C_{r} = \frac{_{n}P_{r}}{r!}$
 = $\frac{n!}{(n-r)!(r!)}$
# Properties
- $\binom{n}{0} = \binom{n}{n}= 1$
- $\binom{n}{1} = \binom{n}{n-1}=n$
- $\binom{n}{k} = \binom{n}{n-k}$
- $\binom{n+1}{k+1} = \binom{n}{k}+\binom{n}{k+1}$
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