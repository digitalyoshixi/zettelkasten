---
tags:
  - windows
  - forensics
---
Used to enable logging of every content ran in [[Powershell]].
# Enabling
Set the [[Registry Key]] to 1:
```
HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging EnableScriptBlockLogging = 1
```