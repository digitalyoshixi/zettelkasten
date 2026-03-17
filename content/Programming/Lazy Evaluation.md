---
tags:
  - programming
aliases:
  - Call-by-need
  - Lazy Loading
  - Lazily
---
An [[Evaluation Strategies|Evaluation Strategy]] which delays the evaluation of an expression until the value is needed.
It avoids repeated evaluations through the use of sharing between threads.
*Evaluation only when required*.
# Methods
- [[delay]]
- [[force]]
# Concepts
- [[Thunk]]