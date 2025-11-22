---
tags:
  - security
  - binary_exploitation
---
If the return address is within the same [[Memory Page]] of your current return pointer, you can directly modify the last 3 values of the return address to move to the address you want.
Read: [[Page Alignment]]