---
tags:
  - malware
  - security
  - windows
aliases:
  - Function Stomping
  - Module Stomping
---
A process to evade [[Memory Scanner|Memory Scanners]] that involves replacing the .text section of a DLL with your own code.
- Indistinguishable from DLL code to memory scanners
# Process
1. [[LoadLibrary()]] of a legitimate DLL
2. Overwrite sections of DLL in memory
3. [[CreateThread]] at the overwritten section

# Comparison

| Property                      | VirtualAlloc (PRV)     | Module Stomp (IMG)                    |
| ----------------------------- | ---------------------- | ------------------------------------- |
| Memory type                   | Private                | Image (mapped file)                   |
| Backing                       | None (pagefile)        | On-disk DLL                           |
| Permissions after setup       | PAGE_EXECUTE_READ      | PAGE_EXECUTE_READ                     |
| MEM_IMAGE flag                | No                     | Yes                                   |
| Appears in loaded module list | No                     | Yes (patched LDR entry)               |
| Stack walk                    | Start address = beacon | Start address = ntdll!TppWorkerThread |
