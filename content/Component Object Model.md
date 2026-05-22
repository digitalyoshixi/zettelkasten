---
tags:
  - windows
aliases:
  - COM
  - COM Object
---
Objects that can be used by different frameworks/languages.
Windows uses them in:
- [[ActiveX]]
- COM+
- [[Distributed Component Object Model]]
Registry keys used:
 - `InprocServer/InprocServer32`
 - `LocalServer/LocalServer32`
 - `TreatAs`
 - `ProgID`
# Structure
![[Component Object Model-20260522140325538.webp]]
A COM consists of:
- Definition
- Various interfaces that all inherit from [[IUnknown Interface]]
# View all COM Objects on System
 ```powershell
 Get-ChildItem HKLM:\Software\Classes -ErrorAction SilentlyContinue | Where-Object {
	$_.PSChildName -match '^\w+\.\w+ -and (Test-Path -Path "$($_.PSPath)\CLSID")
} | Select-Object -ExpandProperty PSChildName
 ```
# Example Usages
```powershell
$ie = new-object -ComObject InternetExplorer.Application
$ie.visible = $true
$ie.Navigate2('www.google.com')
```

```powershell
# Activte the Windows Script Host COM Object by using a ProgID (WScript.Shell)
# We get in return a pointer to the IWshShell Interface
$WshShell = New-Object -comObject WScript.Shell

# Using the CreateShortcut method returns a Shortcut object.
# This path is where the lnk file will be saved
$Shortcut = $WshShell.CreateShortcut("C:\tools\my.lnk")
# Here we specify the location the link points to (what will be executed when we click the file)
$Shortcut.TargetPath = "C:\windows\system32\cmd.exe"
$Shortcut.Save()
```
# Concepts
- [[COM Moniker]]
- [[CLSID]]
- [[TypeLib]]
- [[ProgID]]
- [[AppID]]
- [[InterfaceID]]
# Tools
- [[TypeLibWalker]]
- [[OleViewDotNet]]
- [[MonikerHound]]
# Blogs
- https://mohamed-fakroud.gitbook.io/red-teamings-dojo/windows-internals/playing-around-com-objects-part-1
- https://www.221bluestreet.com/offensive-security/windows-components-object-model/demystifying-windows-component-object-model-com
# Exploits
- [[LeakedWallpaper]]