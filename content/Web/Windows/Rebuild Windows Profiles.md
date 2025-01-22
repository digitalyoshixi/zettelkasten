---
tags:
  - windows
---
Each user profile records desktop preferences like:
- background
- color
- shortcuts
- icons
A corrupt user profile may prevent logging in
May be caused by:
- antivirus tampering
- switching windows versions
# Rebuilt Profiles
### New User
To fix this, you make a new user with [[Windows net]] and copy old profile settings (only copy user preferences, dont copy the entire profile) into the new account with [[Windows Registry|regedit]].
Your profile folder can be found in: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`
![[OS Troubleshooting-20240715191508073.webp]]
Find the folder with the key corresponding to your name
Additionally, set the RefCount key to have the value 0 on the new profile (if you dont have make it DWORD 32bit value)
### Copy Good ntuser.dat
ntuser.dat is a hidden file by default. If you enable hidden files in [[Windows File Explorer]] then you can copy it to a different profile.
ntuser.dat is usually a 5-20MB file.