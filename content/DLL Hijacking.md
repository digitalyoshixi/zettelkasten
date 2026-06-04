---
tags:
  - security
---
Abusing windows DLL search order to place malicious DLL files in those file locations to cause programs to load different DLLs.
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
# Mitigations
- Use fully qualitifed paths
- Require code signing
- Restrict directories of DLL to read-only
- Use [[SetDefaultDllDirectories]] or [[SetDllDirectory]] to restrict directories that system searches for DLL