---
tags:
  - GDB
  - debugging
  - reverse_engineering
---
# GDB typecasting
[https://visualgdb.com/gdbreference/commands/x](https://visualgdb.com/gdbreference/commands/x)

Values will be represented in different formats. Just like languages, we must be the translator.
In gdb, you can print to get values, or you can also use x/format to print in different formats.
An example is x/x 0x0804a001. This prints the value at 0x0804a001 as hexadecimal format.
I recommend representing everything as string if you are examining something null terminated since it will output several memory addresses instead of one. Below are other options to output formatted:

| format | character |
| ---- | ---- |
| hexadecimal | x |
| decimal | d |
| binary | t |
| string | s |
| octal | o |
| unsigned decimal | u |
| floating point | f |
| address | a |
| character | c |
| instruction | i |
You can also include size modifiers aswell after your format. This can be done like: x/ab which prints the address in byte size.
 
| size(32bit example) | character |
| ---- | ---- |
| one byte(8bit) | b |
| halfword(16bit) | h |
| word(32bit) | w |
| giant word(64bit) | g |
Funny thing is that if you chain types or sizes together that conflict, it will accept only the last type/size. Example is:
x/adxgb
will only output in hexadecimal byte format since x and b were the last of their class to be input