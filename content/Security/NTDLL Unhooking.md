---
tags:
  - security
  - windows
---
A technique to restore original code of [[NTDLL]] instead of using the [[Endpoint Detection and Response|EDR]]-injected version of [[NTDLL]].
# Methods
- Directly patch NTDLL in your .text section of your code
- [[Suspended Process Patching]]