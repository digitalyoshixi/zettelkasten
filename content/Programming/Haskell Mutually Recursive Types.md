---
tags:
  - programming
  - haskell
---
A type that depends on another type that depends on the current type
# Example
A tree with branches that contain the values.
```haskell
data Tree a = Empty
			| Node (Branch a) (Branch a)
data Branch a = Branch a (Tree a)

listTree :: Tree a -> [a]
listTree Empty = []
listTree (BNode l r) = (listBranch l) ++ (listBranch r)

listBranch :: Branch a -> [a]
listBranch (Branch v t) = v : listTree t
```