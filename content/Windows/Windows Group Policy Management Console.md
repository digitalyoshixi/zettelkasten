---
tags:
  - windows
aliases:
  - gpmc.msc
  - Group Policy Management
---
A server version of [[Windows Group Policy Editor|gpedit.msc]] that is found on [[Windows Active Directory]]
![[Windows Group Policy Management Console-20240821160430614.webp]]
# Updating Policies
```
gpupdate /force
```
# Viewing Group Policies
```
gpresult /h report.html /f
```