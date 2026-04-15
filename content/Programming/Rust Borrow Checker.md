---
tags:
  - rust
---
A enforcement of memory allocation that ensures:
- All variables initialized before used
- Cant move the same value twice
- Cant move a value while its borrowed
- Cant access a place while its mutably borrowed
- Cant mutate a place where its immutably borrowed
Prevents [[Use After Free|UAF]]
# Ownership
- Every resource, i.e a [[Socket]] has one and only one owner (variable assignment), when owner goes out of scope, the value is dropped
# Moving
- If you pass a variable to a function, the funciton now owns the variable and the original variable is invalidated
# Concepts
- [[Immutable Reference]]