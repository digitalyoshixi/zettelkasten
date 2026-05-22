---
tags:
  - windows
  - programming
---
A method to evade [[Endpoint Detection and Response|EDR]] hooks by using [[Callback]] to functions that dont return.
- EDR will not be able to see that RX section is return at top of stack and program can continue