---
tags:
  - programming
---
![[Drawing 2026-02-02 09.25.17.excalidraw]]
- Suppose that we have a tree like this with the subtree $T$ being heavier than $S$.
- Assume $Weight(S) < Weight(T) \times 2$ Note that this can only happen during insertion (Assumption $(2)$)
- Then, $s+1 < 2(t+1)$
- Note that before rotation, adding an extra node the entire tree $V$ was balanced
- This means $r+1 \leq 3(s + t + 1)$ and, $s+t+1 \leq 3(r+1)$ by defn of balanced in [[Weight Balanced Binary Search Tree|WBT]] (assumption $(3)$)
- Then, on add, there are two ways that the tree $x$ becomes imbalanced: (Assumption $(4)$)
	- Added to $T$: $t \leq 3(s+1)$ and $s+1 \leq 3t$
	- Added to $S$: $t+1 \leq 3s$ and $s \leq 3(t+1)$
- Now, we want to prove that after a left rotation, the tree will become balanced
- We want to show $Weight(left)\leq 3Weight(right)$
- essentially, $r+s+2\leq 3(t+1)$ and $t+1\leq 3(r+s+2)$
- Then, we also want to prove that $X$ and $V$ are balanced ($r+1 \leq 3(s+1)$ and $(s+1) \leq 3(r+1)$)
Proof:
- Assume $(2)$, then $s+1 < s+t+2 = (s+1)+(t+1)$ by $(2)$
- $< 2(t+1) + (t+1) \implies 3(t+1)$ by $(1)$
- Then $r < t \implies$ key structural fact that (Assumption $(5)$)
- $r+s+2 = (r+1)+(s+1) < (t+1) + (s+1)$ by $(1)$
- $< (t+1) + 2(t+1)$ by $(2)$
- $=3(t+1)$
- ...rest of proof
- $t < 3(s+1)$ by $(4)$
- Then, $t+1 \leq 3(s+1)+1 \leq 3(r+s+2)$ (proving that right side of $X$ not too heavy after rotation)