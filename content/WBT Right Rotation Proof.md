---
tags:
  - programming
---
![[Drawing 2026-02-02 09.25.17.excalidraw]]
- Suppose that we have a tree like this with the subtree $T$ being heavier than $S$.
- Assume $Weight(S) < Weight(T) \times 2$ Note that this can only happen during insertion
- Then, $s+1 < 2(t+1)$
- Note that before rotation, adding an extra node the entire tree $V$ was balanced
- This means $r+1 \leq 3(s + t + 1)$ and, $s+t+1 \leq 3(r+1)$ by defn of balanced in [[Weight Balanced Binary Search Tree|WBT]]