---
tags:
  - programming
  - haskell
---
A datatype that is recursive.
# Example
```haskell
data LList = Nil | Node (Int, LList) deriving Show
llist = Node (1, Node (2, Node(3, Nil)))

llistLen :: LList -> Int
llistLen Nil = 0
llistLen (Node (_, rest)) = 1 + llistLen rest
```