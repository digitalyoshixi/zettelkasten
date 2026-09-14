---
tags:
  - software
aliases:
  - DLL
  - Shared Library
---
An executable that cannot run on its own. 
It can only export functions for use in other programs.
# Concepts
- [[Linker|Linking]]
- [[__declspec]]
- [[DLL Ordinal]]
- [[System-Wide DLL Base]]
- [[DLLMain]]
- [[Running DLL]]
- [[DLL Loader Lock]]
# Attacks
- [[DLL Hijacking]]
- [[Local DLL Injection]]
- [[Remote DLL Injection]]
- [[Manual DLL Injection]]
# Guides
- [[DLL Export Code]]
- [[DLLMain Thread Execution Code]]
# DLL Search Process
1. Search current directory
2. Search [[System32]]