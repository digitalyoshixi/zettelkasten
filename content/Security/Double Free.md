---
tags:
  - security
  - binary_exploitation
---
Calling free on the same free'd chunk can add it to the [[Heap Free List]] twice.
[[Fast Bin]] are vulnerable.
# Mitigations
- Malloc tries to prevent trivial double frees (2 in a row)
- Tcache checks an entire list (only 7)
- Tcache has a key field that will check if its zero, if it is, then it crashes since it knows double free has happened
# Alternatives
- [[Staggered Double Free]]