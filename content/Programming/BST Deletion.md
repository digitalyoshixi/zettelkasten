---
tags:
  - proofs
---
# Case 1 - Leaf
Delete the leaf and you are done
# Case 2 - Node with 1 child
Swap the parent of the node with the child node, and then remove the original node
# Case 3 - Node with 2 children
1. Find the smallest in the right subtree of the node
   ![[BST Deletion-20250305163425668.webp|344]]
   Go to the right subtree then continue going down the left branch
2. Replace the node to delete with the one you found
   ![[BST Deletion-20250305163544112.webp|279]]