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
# Concepts
- [[Immutable Reference]]