---
tags:
  - ricing
  - windows
---
# Komorebi
This is simply the tiling window manager. `komorebi.exe` is the window manager. `komorebic.exe` daemon that manages the commands to the window manager.
If you want hotkeys, you need to use [[AutoHotKey]] or [[whkd]].

# Installation
`Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem' -Name 'LongPathsEnabled' -Value 1`
`winget install LGUG2Z.komorebi`
`winget install LGUG2Z.whkd`
Restart windows
### Configuration 
`komorebic quickstart`
![[Komorebi(Tiling Manager)-20240303232410726.webp]]
