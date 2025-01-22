---
tags:
  - math
---
A method of representing permutations through using a diagram of possible choices.
![[Pasted image 20230912144431.png]]
Resembles a real life tree.
Each decision is a node, each final node is a branch.

## Counting branches with [[Multiplicative Counting Principle]]
The more options you have in a tree diagram, the more complex it is to count. You dont need to count each branch if your tree is a regular tree with each branch at same hierarchy, you can do simple multiplication
### Example
For example, the problem may be making a sandwich: 
Meat choices: Ham, Pastrami, Salami, Turkey
Bread choices:  Plain, Whole-wheat, Rye
Lettuce: Iceberg, Greenleaf
Sauces: Dill, Barbeque, Mustard
There are 4 meat choices, 3 bread, 2 lettuce, 3 sauces.
to get all options: multiply each # of options with each next # of options.
4\*3\*2\*3 = 72
72 branches.

