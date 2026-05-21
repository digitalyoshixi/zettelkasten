---
tags:
  - malware
---
A tool to load [[Shellcode]] from a file and execute it.
# Process
1. Allocate memory for shellcode ([[VirtualAlloc]])
2. Write shellcode to memory ([[memcpy]])
3. Make memory executable ([[mprotect]])
4. Execute the memory ([[C Function Pointers]] execution)