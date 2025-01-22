---
tags:
  - windows
aliases:
  - Windows UAC
  - Windows User Accounts
---
Windows utilizes UAC for certain programs, which prevents execution unless the user is a local [[Windows Administrator]]. 
[[Linux]] uses [[sudo]]
![[Windows User Accounts Control-20240706221312632.webp]]
Shows up when:
- Installing and uninstalling applications
- Installing a driver
- Adjusting [[Windows Defender Firewall]] settings
- Changing user's account type
- Switching to another user's directory
# UAC Levels
UAC frequency can be changed in [[Windows Control Panel]],
![[Windows User Accounts Control-20240706185419976.webp]]
![[Windows User Accounts Control-20240706221536803.webp|538]]
1. Always Notify. UAC prompt shows up everytime administrator privileges are required
2. Notify only when apps/programs make changes
3. Dont notify when I make changes to windows settings
4. Never notify
This feature can also be toggled on or off in the [[Windows Registry]]
# UAC Run
To run as administrator:
- Right click app and select "Run as Administrator"
- CTRL + SHIFT + LMB on app
- In [[Windows Run]], hold CTRL + SHIFT + Enter