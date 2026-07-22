---
tags:
  - malware
  - security
  - windows
aliases:
  - Function Stomping
  - Module Stomping
---
A process to evade [[Memory Scanner|Memory Scanners]] that involves replacing the .text section of a DLL with your own coe
# Process
1. [[LoadLibrary()]] of a legitimate DLL
2. Overwrite sections of DLL in memory
3. [[CreateThread]] at the overwritten section