---
tags:
  - windows
  - os
aliases:
  - Process Memory Space
  - Process Memory
---
The process memory layout of a process in [[Random Access Memory|RAM]] loaded by the [[Operating System|OS]].
# Memory Types
- [[Private Memory]]
- [[Mapped Memory]]
- [[Image Memory]]
# Memory Space
![[Windows Virtual Memory Space-20260614010948246.webp]]
- Program Image is the loaded executable
- PEB/TEB contain process and thread metadata
- Kernel land is OS memory inaccessible in user mode