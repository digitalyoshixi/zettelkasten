---
tags:
  - security
---
Enabling [[Thread Local Storage|TLS]] [[Lightweight Directory Access Protocol|LDAP]] authentication
# Enabling
```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\NTDS\Parameters" -Name "LDAPServerIntegrity" -Value 2 -Type DWord
```
# Monitoring
- Monitor event ID 2889 after [[Windows Enable LDAP Diagnostics]]