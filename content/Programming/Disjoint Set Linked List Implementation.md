---
tags:
  - programming
---
Implementing [[Disjoint Set]] using [[Linked List]].
# Implementation
- Each set is a linked list
- `make-set()` make a linked list
- `x.set` is a pointer to x's owning list
- `find-set(x)` will follow the pointer
- `union(S1,S2)` merges linked lists, always move smaller list into the larger one.
# [[Amortized Time|Amortized Analysis]]
- Finding `x.set` takes at most $\log(n)$ times (walking up the tree)
- There are $n$ set fields to update
- Total number of updates is at most $n\log n$
- Amortized time for $k$ operations `make-set()`, `find-set()`, `union()` overall $O(\log n)$