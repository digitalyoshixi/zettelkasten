---
tags:
  - math
---
Depending on the number base we use, numbers may look very different. We have binary, octal, hexadecimal too. These are the main ones we use to display data.

  

From left to right. 0000. digit on the leftmost side will hold the smallest value.

They go like this:

leftmost is base^0

2nd leftmost is base^1

3rd leftmost is base^2

and on and on

  

we cant ever go to use the digit 2 in binary because, the number system caps out at 1. only 2 types of digits in binary, as like only 8 in octal and only 16 in hex. There is no reason to use any more when 100 = 4, you don’t need 20 = 4 aswell.

  

### Binary → Octal → Hex conversion

An octal is 3 digits of binary, a hex is 4 digits. This is why.

2^3 = 8

2^4 = 16

so if you want to convert binary to octal or hex, you need to seperate the digits in pairs.

From left to rightmost

1001010110 base2

split it up

001 001 010 110

then convert to octal since pairs of 3

1126

  

again for hexadecimal

1001010110

split into pairs of 4

0010 0101 0110

then convert to hexadecimal

256

  

### Hex for colors

Yknow RGB goes up to 255. and 2 hex goes to 255. so just have 6 hex digits for RGB. FFFFFF is white, 000000 is black, FF0000 is red, so on so forth.