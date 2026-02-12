---
tags:
  - programming
  - esolang
aliases:
  - Closure
---
A record storing a [[Subroutine|Function]] and its [[Function Environment]] in a function such that:
- Subsequent calls to the same closure can have the same [[Function Environment]]
- Functions can oftentimes pass their [[Function Environment]] to outer closure

Languages that implement closures often can also handle inner-closures, similar to [[List Processor|LISP]].
Often very expensive to implement memory-wise.
# Inner vs Outer Closure
![[Function Closures-20260208045546675.webp|477]]
### Inner Closure
The region within a function
### Outer Closure
The region surrounding a function