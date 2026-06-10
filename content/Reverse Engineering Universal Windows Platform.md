---
tags:
  - windows
  - reverse_engineering
aliases:
  - Reverse Engineering UWP
---
# Copying Files
1. Get the path
```powershell
Get-AppxPackage *ProgramName* | Select-Object InstallLocation, PackageFullName, PackageFamilyName
```
2. Copy to a directory
```
robocopy /B /E /COPY:DAT "Pathyougot" "C:\Users\David\Downloads\Tempdir"
```