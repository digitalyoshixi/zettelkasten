---
tags:
  - firmware
  - security
aliases:
  - ETW
---
The service that manages event collection to be read in [[Windows Event Viewer]].

# Patching
- Replace call with [[No Operation|NOP]]
- Replace call with early return (`xor eax, eax; ret`)
- Patch [[NtTraceEvent]]
- Modify [[System Service Number|SSN]] before call to [[NtTraceEvent]]