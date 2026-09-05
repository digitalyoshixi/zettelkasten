---
tags:
  - security
  - blockchain
aliases:
  - RLP
---
A encoding method used to encode data structures into a space efficient format used in [[Ethereum]] network.
# Structure
- For single values, starts with `0x80` + length of string
- For lists, starts with `0xc0` + length of list
# Example
![[Recursive Length Prefix-20260518005722672.webp]]