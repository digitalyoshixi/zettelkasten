---
tags:
  - windows
---
These are the file that make up the [[Windows Registry]]. 
Hives are located at:
- `\%SystemRoot%\System32\config`
- Each user account folder
# Hives List
- `SAM` : contains information about [[Security Accounts Manager|SAM]] like user accounts, passwords, creation, login dates, etc
- `SECURITY`: contains security info stored in key `HKLM\SECURITY`
- `SOFTWARE`: contains keys about computer software configuration
- `SYSTEM`: contains info stored in `HKLM\SYSTEM` about computer system config like event log policies
- `DEFAULT`: contains default system info stored in key `HKEY_USERS\DEFAULT`
- [[Ntuser]]