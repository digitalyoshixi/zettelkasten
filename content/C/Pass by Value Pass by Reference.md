---
tags:
  - c
---
# Pass by value
A copy is sent as an argument.
The function can **NOT** modify the original value.
Applies for:
- int
- bool
- char
- double/float
Only is possible if the current datatype is less than the wordsize on the current architecture.
# Pass by reference
The address of the start is sent. You are able to modify it directly by dereferencing.
Applies for:
- [[C Strings]] <- python does the same, but python blocks modification
- [[C Structures]]
