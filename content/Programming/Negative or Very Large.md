---
tags:
  - assembly
  - os
---
This is a common problem when working with hexadecimals. How do we tell if a hex is a negative number or actually a very large number?

If you have a hex with value 0xFFFFFFFF - 0x00000001(4294967295 - 1) then the output is fffffffe.

Additionally, if you subtract 5-7, then you also get fffffffe

These 2 are completely different numbers

  

To solve this problem you must do the following steps:

1. Use subs instead of sub operator. Subs will carry the flag to cpsr
    
2. ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv9z_tmp_91e8546bc16520a5.png)
    

cpsr register will tell you if it is negative or not. If the N flag is highlighted
