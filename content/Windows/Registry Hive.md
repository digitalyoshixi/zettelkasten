---
tags:
  - windows
aliases:
  - HKCU
  - HKLM
  - HKCR
  - HKU
  - HKCC
---
These are the file that make up the [[Windows Registry]]. 
Hives are located at:
- `\%SystemRoot%\System32\config`
- Each user account folder
# Hives List
### HKEY_CLASSES_ROOT (HKCR)
Includes the standard class objects used by Windows. These objects can be for files like defining JPG image file.
`HKEY_CLASSES_ROOT\.jpg` (or `HKEY_CURRENT_USER\Software\Classes\.jpg` for backwards compatibility) covers user-specific associations for JPG files.
### HKEY_CURRENT_USER (HKCU)
Stores personalized settings for current user like:
- desktop colors
- screensavers
- desktop contents
### HKEY_USERS (HKU)
Same information as`HKEY_CURRENT_USER`, but for all users
### HKEY_LOCAL_MACHINE (HKLM)
Contains data for user-independent system configurations. Includes:
- All devices
- All programs
### HKEY_CURRENT_CONFIG (HKCC)
If values in `HKEY_LOCAL_MACHINE` can have 1 or more option - such as 2 monitors, then this key defines which one is currently being used.