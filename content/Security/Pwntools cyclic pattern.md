---
tags:
  - binary_exploitation
  - security
---
A stream of bytes that can be queried such that a substring of 4-bytes has a unique location.
```python
pwn.cyclic(128) # return a bytes object of 128 bytes
```
![[Pwntools cyclic pattern-20250207011404473.webp]]
# `pwn.cyclic_find()`
![[Pwntools cyclic pattern-20250207011550993.webp]]