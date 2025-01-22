---
tags:
  - math
aliases:
  - Arrangements
excalidraw-plugin: Multinomial Coefficient
---
For certain cases, we are asked to find permutations of items where some items are repeated.
- Same letters in string
- Dividing entities into groups

The number of permutations of a set *n* containing *a* identical object of one kind, *b* identical objects of another kind, *c* identical objects of another kind and so on,
$$\frac{n!}{a!b!c!}$$
# Examples
### Example 1
For example, if we were asked for the permutations of the word: `ROOM` then we would encounter there are 2 O's
A word does not care about the type of O given, so an O in the second place is the same as an O in the first.
The total permutations of ROOM is 12. Not 24
We use [[Box Occupant Based Thinking]] And clump the 2 O as the same thing.
total permutations /# of times it is repeated
4! / 2! = 12
### Example 2
How many arrangements of the word `bookkeeper` is there?
10 characters all together
2 o's
2 k's
3 e's
10!/(2!2!3!) = 151200
