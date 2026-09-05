---
tags:
  - ai_safety
---
A proposed protocol used to develop safe AI systems.
Does not work if AI only lies about its own vulnerabilities
- In backdoored code, name variables differently
- In backdoored code, use while loops where for loops would work better
# Protocol
- Use untrusted AI to check for suspicious code as the monitor
- Test untrusted AI on fake backdoors
- If monitor acts like backdoored code is fine, then we know it is [[Misalignment|Misaligned]]