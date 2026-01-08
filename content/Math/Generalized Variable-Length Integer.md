---
tags:
  - programming
  - math
aliases:
  - Integer Threshold Function
  - VarInts
  - Variable-Length Quantity Encoding
---
A encoding system for encoding multiple digits into a string.
# Algorithm
Every digit of a number must be greater or equal to the threshold $t(i)$ at a the given string position $i$, except for the last digit which must always be smaller
### Threshold Function
$t(i) : \mathbb{Z} \to \mathbb{Z}$
A function that returns the threshold for a given index of a string
# Decoding Example
![[Generalized Variable-Length Integer-20251230041627943.webp]]