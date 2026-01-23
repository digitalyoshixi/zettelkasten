---
tags:
  - linux
---
A hexdump program to print in octal.
# Example Usage
Printing:
- 2 byte chunks after the 44th byte in decimal
```
od -A d -j 44 -t d2 short.wav
```