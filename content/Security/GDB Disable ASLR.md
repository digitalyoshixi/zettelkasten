---
tags:
  - GDB
  - debugging
---
# Non SUID
```
set disable-randomization off
```
# With [[suid]]
```
setarch x86_64 -R /bin/bash
```