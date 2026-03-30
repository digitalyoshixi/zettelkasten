---
tags:
  - forensics
  - windows
---
These are registry keys that store details about all folders a user has accessed.
- Can identifier accessed directories
- Can reveal hidden or deleted files and folders
```
HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\BagMRU
HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\Bags
NTUSER.DAT\Software\Microsoft\Windows\Shell
NTUSER.DAT\Software\Microsoft\Windows\ShellNoRoam
USRCLASS.DAT\Local Settings\Software\Microsoft\Windows\Shell
USRCLASS.DAT\Local Settings\Software\Microsoft\Windows\ShellNoRoam
```
# Tools
- Use [[ShellbagsExplorer]]