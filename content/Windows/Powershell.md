---
tags:
  - windows
aliases:
  - .ps1
  - pwsh
---
The [[Shell]] and scripting language for windows devices.
Used primarily in automation of windows and [[Windows Active Directory|Active Directory]] functions.
Powershell is cross platform now `pwsh`
# Connect to [[Exchange Admin Center]]
```
Install-Module -Name ExchangeOnlineManagement -Scope CurrentUser
```
```
Connect-ExchangeOnline -UserPrincipalName admin@catbird.net -Device
```