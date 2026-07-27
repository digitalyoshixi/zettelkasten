---
tags:
  - windows
  - security
---
A [[Privilege Escalation]] attack wherein normal users can read [[Security Accounts Manager|SAM]].
Caused by sloppy coding giving excessive permissions to folders and files for normal users.
# Testing
```
icacls C:\Windows\System32\Config\SAM
```
If BUILTIN\users:(I)(RX) appears, then it is vulnerable
