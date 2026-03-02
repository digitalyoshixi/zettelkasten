---
tags:
  - programming
---
# Algorithm
`delete(T,k)`
1. Find node with key $k$, call it $w$
2. If $w$ is a leaf, remove it
3. If $w$ has a single child, replace with the child
4. If $w$ has two children, replace with [[Successor Node]], successor's parent adopts successor's right child
5. Backtrack up to root and update sizes