---
tags:
  - windows
  - malware
---
Not to be confused with [[Windows AutoPlay]]
These are [[Registry Key]] that can be used to set programs to automatically run on system startup.
# Autorun Registry Keys
```
C:\Windows\system32\config\Software\Microsoft\Windows\CurrentVersion\Run
C:\Windows\system32\config\Software\Microsoft\Windows\CurrentVersion\RunOnce
C:\Windows\system32\config\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
C:\Windows\system32\config\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\RunOnce
C:\Users\<User>\ntuser.dat\Software\Microsoft\Windows\CurrentVersion\Run
C:\Users\<User>\ntuser.dat\Software\Microsoft\Windows\CurrentVersion\RunOnce
```
# Viewing Autoruns
A diagnostic software for viewing which software automatically starts up in windows.
Windows has alot of trouble pinpointing auto-startup software due to its scattered ecosystem and its push on [[Backwards Compatability]] allowing old features to remain present.
# Installation
https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns