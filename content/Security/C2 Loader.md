---
tags:
  - malware
aliases:
  - Shellcode Loader
---
A tool to load [[Shellcode]] from a file and execute it.
# Process
1. Allocate memory for shellcode ([[VirtualAlloc]])
2. Write shellcode to memory ([[memcpy]])
3. Make memory executable ([[VirtualProtect]])
4. Execute the memory ([[C Function Pointers]] execution or [[CreateThread]])
