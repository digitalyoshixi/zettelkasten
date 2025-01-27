---
tags:
  - reverse_engineering
  - x86
---

### Part 28 ASM code 3 mem->reg

Here we use the .data segment. We declare a constant value by writing constant indented and then whatever the value of constant is

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivbb_tmp_6c9ba4ddb994052a.png)

We later can move this constant value into a register

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivbb_tmp_a3672f660ddb7289.png)

This is moving a memory variable into a register