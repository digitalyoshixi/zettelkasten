---
tags:
  - programming
---
A [[Haskell Currying|Curried]] version of a [[Haskell Value Constructor]].
```haskell
data BTree a = Empty | Node (a, BTree a, BTree a)
-- curried:
data BTree a = Empty | Node a (BTree a) (BTree a)
```