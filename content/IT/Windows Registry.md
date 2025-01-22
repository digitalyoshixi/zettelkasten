---
tags:
  - windows
aliases:
  - Registry Editor
  - regedit
---
A database of critical information in a Windows system.
Stores:
- Hardware information
- Network information
- User preferences
- File types
- Passwords
- Desktop color
Almost everything in windows is configured through the registry, or configures the registry.
# Registry Editors
### CLI
- `reg`
- `revsvr32`
### GUI
- `regedit`
# Hive Locations
Registry files are called *hives*.
hives are located at:
- `\%SystemRoot%\System32\config`
- Each user account folder
# Keys
These are specific properties relegated to specific programs or features. 
Root keys are the keys that are the first node. Subkeys branch off of root keys.
Every key may branch off to other subkeys or values.
### Root Keys
##### HKEY_CLASSES_ROOT
Includes the standard class objects used by Windows. These objects can be for files like defining JPG image file.
`HKEY_CLASSES_ROOT\.jpg` (or `HKEY_CURRENT_USER\Software\Classes\.jpg` for backwards compatibility) covers user-specific associations for JPG files.
##### HKEY_CURRENT_USER
Stores personalized settings for current user like:
- desktop colors
- screensavers
- desktop contents
##### HKEY_USERS
Same information as`HKEY_CURRENT_USER`, but for all users
##### HKEY_LOCAL_MACHINE
Contains data for user-independent system configurations. Includes:
- All devices
- All programs
##### HKEY_CURRENT_CONFIG
If values in `HKEY_LOCAL_MACHINE` can have 1 or more option - such as 2 monitors, then this key defines which one is currently being used.
# Values
![[Windows Registry-20240705181225842.webp]]
The data that can be changed in the registry.
Their types include:
- String
- Binary (16bit)
- DWORD (32bit)
- QWORD (64bit)