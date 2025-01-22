---
tags:
  - reverse_engineering
---
### Find Input that leads to address
```
simgr.explore(find=0x.....)
print(simgr.found) # print all inputs that lead to this address
```