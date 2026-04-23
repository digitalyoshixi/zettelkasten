---
tags:
  - programming
  - debugging
aliases:
  - GDB Forks
---
# Set Debug Modes
```c
set follow-fork-mode <mode>
```
With `<mode>` as:
- `parent`: follow parent process
- `child`: follow child process
# Simulatenous Debugging with