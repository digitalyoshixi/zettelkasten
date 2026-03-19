---
tags:
  - programming
aliases:
  - Binary Heap
  - Nearly Complete Binary Tree
---
A [[Binary Tree]]-based data structure where all levels are mostly filled (except sometimes the lowest) starting from left to right
![[Heap-20260222205303684.webp]]
### Zero Indexed Language Parent/Children
- left = `2i + 1`
- right `2i + 2`
- parent `Math.floor(i-1/2)`
# Types
- [[Heap Sort]]
  [[Max-Heap]]
- [[Min-Heap|Min-Heap]]
# Height
$Height = \log(n)+1$
