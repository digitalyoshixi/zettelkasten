---
tags:
  - reverse_engineering
  - x86
---

### Part 31 ASM code 4 reg->mem

So, we remade the .section .data constant from last assembly code(part 28).

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivbe_tmp_a7aafd00b8d9a69a.png)

Then we have this line that moves to that variable declared from a registry. Rather straight forwards idk why im writing this.

Anyhow, during debug we are able to print memory using the method of “p ([type]) [variable]”

An example for this would be “p (int) constant”

  

  

To set memory variables to different values, follow 2.5 steps

1. P &variable. This is the address
    
2. set *address = value. Using address from first part and setting variable to new value
    

2.5. Alternate method. set {int}address = value