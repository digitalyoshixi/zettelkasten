---
tags:
  - programming
  - windows
---
A mechanism that prevents you from having multiple threads while DLL is being loaded.
![[DLL Loader Lock-20260914154809681.webp|341]]
- In general, only initialization code should be performed, best to use [[Lazy Evaluation|Lazy Initialization]]
- If you want to execute code during load, you must create a [[Process Control Thread|Thread]] or queue a [[Asynchronous Procedure Call]]