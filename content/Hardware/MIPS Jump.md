---
tags:
  - programming
---
This is a J-Type instuction in [[MIPS Instruction Types]].
Will change [[Program Counter Register|PC]] to be the address given.
# Jump Process
1. Extract the 26-bits from the address
   ![[MIPS Jump-20250815022733724.webp]]
2. Add an extra 2 bits at the end
3. Add the first 4-bits of the current PC to the front
   ![[MIPS Jump-20250815022744225.webp]]
4. This is your new PC
   ![[MIPS Jump-20250815022757731.webp]]