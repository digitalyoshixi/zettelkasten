---
tags:
  - security
aliases:
  - DLL Sideloading
---
The process of inserting a [[Dynamic Linked Library|DLL]] into a running program through [[LoadLibrary()]].
# Classic Pattern
- [[VirtualAllocEx]]
- [[WriteProcessMemory]]
- [[CreateRemoteThread]]
# Target DLLs
- Application DLLs
- DLLs that are loaded from working directories (use [[Procmon]])
# Loading Methods
- [[DLL Export Sideloading]]
- [[DLLMain Sideloading]]
- [[Export Proxy Sideloading]]