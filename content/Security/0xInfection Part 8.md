---
tags:
  - 0xInfection
  - math
---

### Part 8: Bytes, Words, Double Words, etc…

Typically we say bytes for memory and bits for downloading. A byte is 8 bits. And a bit is just one transistor(1 or 0). A byte is also referred to as a word.

1 byte = 1 word = 8 bit

2 byte = 2 word = 16 bit

4 byte = double word = 32 bit

8 bytes = quad word = 64 bit

Value of a 8byte can be the same as a 4 byte, but a 4 byte cannot always have the value of an 8 byte. Eg. 31 bit can be 8 bytes but 33 bit can't be 4 bytes.

Every byte also has its own unique address. These are always hexadecimal values.

A hexadecimal to byte can be understood as the digits of a hexadecimal/2.

So hexadecimal 0xffffffff has 8 digits, it is stored in 4 bytes.

Hexadecimal 0xffff is 4 digits so it is stored in 2 bytes