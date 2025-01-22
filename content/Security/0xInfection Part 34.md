---
tags:
  - 0xInfection
  - x86
---
### Part 34 Indirect addressing

Indirect addressing is how to get the next value of a list. Simply add 4 bytes to this address to find the address of the next value.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivbg_tmp_cec5347e2bdc1220.png)

Pretend there is a list of constants. The code above moves the first index value into register eax. The second line moves memory address into edi, then alters the second index to be 25 and then changes list index of itself to be the second index.