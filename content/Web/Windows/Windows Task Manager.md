---
tags:
  - windows
  - os
aliases:
  - taskmgr.exe
---
`CTRL+SHIFT+ESC`
A windows tool to view all [[Process|Processes]] and configure startup apps.
# Tabs
### Performance
![[Windows Task Manager-20240705212056579.webp]]
You can view the specs and usage for all your hardware
### Users
You can view the computer resource allocation for each user and sign other users out if you are a local administrator 
![[Windows Task Manager-20240705211935094.webp]]
### Details
![[Windows Task Manager-20240705212402609.webp|352]]
A more detailed view of each individual process including their:
- [[Process|PID]]
- User
### Services
Opens [[Windows Services]]
# Extra
### Task Manager Program Stray Apps
[https://www.thewindowsclub.com/what-is-program-in-startup-tab-in-task-manager](https://www.thewindowsclub.com/what-is-program-in-startup-tab-in-task-manager)
![[Windows Task Manager-20240705210210738.webp|354]]
Sometimes when you uninstall software, the registry keys persist and the Task Manager will keep the software's instance even though it does not exist anymore.
Open [[Windows Registry|Registry Editor]] and see if you can delete the software keys in `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run