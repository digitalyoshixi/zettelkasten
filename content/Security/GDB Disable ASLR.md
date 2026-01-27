---
tags:
  - GDB
  - debugging
---
# Non SUID
During gdb instance:
```
set disable-randomization on
```
# With [[suid]]
Create a non SUID shell with:
```
setarch x86_64 -R /bin/bash
```