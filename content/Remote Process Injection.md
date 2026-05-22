---
tags:
  - programming
  - malware
---
Injecting code into a external running process.
# Classic Pattern
1. [[VirtualAllocEx]]
2. [[WriteProcessMemory]]
3. [[VirtualProtectEx]]
4. [[CreateRemoteThread]]