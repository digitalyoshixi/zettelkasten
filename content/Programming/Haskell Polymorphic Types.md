---
tags:
  - haskell
---
Creating your own type that uses a generic type. Essentially, a type that is just a structure.
# Example (Linked List)
```haskell
data LList a = Nil | Node (a, LList a) deriving Show

llist1 = Node (1, ,Node (2, Node(3, Nil)))
llist2 = Node ('1', ,Node ('2', Node('3', Nil)))

llistLen :: LList t -> Int
llistLen Nil = 0
llistLen (Node (_,rest)) = 1 + llistLen rest
```