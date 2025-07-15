---
tags:
  - assembly
  - programming
---
# Caller-Saved Registers
These are registers that be pushed to the [[Stack]] before function call, because the callee will modify them.
1. Registers `$t0-$t7` are caller saved
2. Registers `$a0-$a3` are caller saved
If you don't care about these registers, then you dont need to push them.
# Callee-Saved Registers
These are registers that are pushed to the [[Stack]] if the callee wants saved variables between calls.
1. Registers `$s0-$s7` are saved temporaries