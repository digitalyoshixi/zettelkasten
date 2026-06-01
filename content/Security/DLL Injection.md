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
- Application DLLs that are signed by third parties
- DLLs that are loaded from working directories (use [[Procmon]])
- DLLs that are non-default signed by microsoft (not in [[System32]], not a [[LOLBIN]])
### For [[Command and Control Server|C2]]
- Loads [[winhttp]] or [[wininet]]
- Reaches out to internet in some way
- Makes [[Lightweight Directory Access Protocol|LDAP]] calls
# Loading Methods
- [[DLL Export Sideloading]]
- [[DLLMain Sideloading]]
- [[Export Proxy Sideloading]]