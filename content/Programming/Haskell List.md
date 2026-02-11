---
tags:
  - programming
  - haskell
---
A arbitrary size collection of the same datatype.
```
[1,2,3,4]
['a','b','c']
```
# Datatype
- `[Int]` : Int list
- `[a]` : list of any type ([[Haskell Polymorphism]])
# Functions
- [[Haskell head]]
- [[Haskell tail]]
# Underlying Implementation
```haskell
[1,2,3,4]
-- is actuall syntactic sugar for
1:2:3:4:[]
```