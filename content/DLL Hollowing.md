---
tags:
  - malware
  - security
  - windows
aliases:
  - Function Stomping
  - Module Stomping
---
# Process
1. [[LoadLibrary()]] of a legitimate DLL
2. Overwrite sections of DLL in memory
3. [[CreateThread]] at the overwritten section