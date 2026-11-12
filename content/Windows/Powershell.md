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
# [[Exchange Admin Center]]
### Connect to [[Exchange Admin Center]]
```
Install-Module -Name ExchangeOnlineManagement -Scope CurrentUser
```

```bash
# for windows only
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Import-Module ExchangeOnlineManagement
```

```
Connect-ExchangeOnline -UserPrincipalName admin@catbird.net -Device
```
### Disconnect [[Exchange Admin Center]]
```
Disconnect-ExchangeOnline
```
### Check Reject Send
```
Get-Organizationconfig | grep -E "Name|RejectDirectSend"
```