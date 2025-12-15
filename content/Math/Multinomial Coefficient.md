---
tags:
  - statistics
aliases:
  - Permutations with Identical Items
  - Arrangement
---
A notation used to divide combinations into smaller sub-boxes.
# Notation
$$
C_{a,b,c}^{n} = \binom{n}{a, b, c} = \frac{n!}{a!b!c!}
$$
Where:
- $a+b+c = n$
# Example
### Example 1
Split a group of 12 people into 3 groups of 2 people, 5 people and 5 people
##### Soln
$$
\frac{1}{2!}\binom{12}{2, 5, 5} = \frac{12}{2!2!5!5!}
$$
With the $\frac{1}{2!}$ corresponding to repeated groups
### Example 2
For example, if we were asked for the permutations of the word: `ROOM` then we would encounter there are 2 O's
A word does not care about the type of O given, so an O in the second place is the same as an O in the first.
The total permutations of ROOM is 12. Not 24
We use [[Box Occupant Based Thinking]] And clump the 2 O as the same thing.
total permutations /# of times it is repeated
4! / 2! = 12
### Example 3
How many arrangements of the word `bookkeeper` is there?
10 characters all together
2 o's
2 k's
3 e's
10!/(2!2!3!) = 151200