---
tags:
  - windows
aliases:
  - Registry Subkey
---
These are specific properties relegated to specific programs or features.
Root keys are the keys that are the first node. Subkeys branch off of root keys.
Every key may branch off to other subkeys or values.
# Important Keys
- `SAM`: Contains information about [[Security Accounts Manager|SAM]] like user accounts, passwords, creation, login dates, etc
- `SECURITY`: contains security info stored in key `HKLM\SECURITY`
- `SOFTWARE`: contains keys about computer software configuration
- `SYSTEM`: contains info stored in `HKLM\SYSTEM` about computer system config like event log policies
- `DEFAULT`: contains default system info stored in key `HKEY_USERS\DEFAULT`
- [[Ntuser]]
- `Control Panel` located under `HKEY_CURRENT_USER\Control Panel`
- `Run` located under `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`