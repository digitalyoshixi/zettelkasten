---
tags:
  - programming
  - malware
---
[[Thread Hijacking]] for a remote process
# Classic Pattern
1. [[VirtualAllocEx]]
2. [[WriteProcessMemory]]
3. [[VirtualProtectEx]]
4. [[GetThreadContext]]
5. [[SetThreadContext]]
6. [[ResumeThread]]