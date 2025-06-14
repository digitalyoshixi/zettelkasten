---
tags:
  - reverse_engineering
---
# Procedures
1. Have the language reference on standby, to refer to the required arguments and return, for easier translation of assembly
2. Try to convert all assembly into original code
3. Always try and sync your debugger's offsets with your disassemblers offsets. ([[Binary Ninja Rebase Base Address]])
4. Most disassemblers have a highlight feature for [[Basic Block|Blocks]]. Use that to signal which code is irrelevant and which is important