---
tags:
  - security
---
A tool to find the parameters of a [[Cyclic Redundancy Check|CRC]] algorithm from a given number of samples.
# Reverse CRC
```
reveng -w32 -s \
  "52 45 43 00  02 00 00 00  04 00 00 00  05 00 00 00  D9 D1 49 38" \
  "52 45 43 00  02 00 00 00  06 00 00 00  07 00 00 00  2F 1E 65 D0" \
  "52 45 43 00  02 00 00 00  08 00 00 00  09 00 00 00  2E 7B 30 25" \
  "52 45 43 00  02 00 00 00  0A 00 00 00  0B 00 00 00  D8 B4 1C CD"
```
