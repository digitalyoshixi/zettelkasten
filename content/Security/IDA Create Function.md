---
tags:
  - reverse_engineering
---
If IDA fails to identify a function, you can force it to analyze the current disassembly with `P`.
# Quick Register Size Fix
You can define the function with `ALT+P` and specify that saved registers are 4-bytes and that registers are [[rbp|ebp]] based.