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