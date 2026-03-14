---
tags:
  - programming
aliases:
  - Method Resolution Order
  - MRO
---
The issue of method resolution order in cases where a class has [[Multiple Inheritance]] and multiple parents have the same [[Function Signature]].
![[Diamond Problem-20260312165807311.webp]]
# Solutions
- [[Python]] uses depth-first left-to-right search to find method to execute
- Java does not support [[Multiple Inheritance]]