---
tags:
  - 0xInfection
  - GDB
---
### Part 36 gdb haxoring

To find the address of a variable, then you will need to type &variablename.

From there, you can get the value at the address by typing *address

You CANNOT do *(&variablename) because &variablename returns a data variable type so it will have a bunch of junk

You will be able to do set *address = value.