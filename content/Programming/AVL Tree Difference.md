---
tags:
  - programming
---
A [[AVL Tree]] that contains key/value pairs that are in $T_{1}$, but not in $T_{2}$
# Pseudocode
```pascal
diff(T1, T2):
    if T1 is empty: return empty
    if T2 is empty: return T1

    // Use T2's root as pivot
    let (L2, _, R2) = expose(T2)   // left subtree, root key k2, right subtree
    k2 = root key of T2

    let (L1, b, R1) = split(T1, k2)
    // L1 = T1 keys < k2,  R1 = T1 keys > k2
    // b = whether k2 ∈ T1 (we discard it — k2 is in T2)

    left  = diff(L1, L2)
    right = diff(R1, R2)

    return join2(left, right)      // join without a middle key
```