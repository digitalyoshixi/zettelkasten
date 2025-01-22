---
tags:
  - windows
aliases:
  - taskschd.msc
---
Poorly made software equivalent to a [[Cron]] job for windows.
Dont use this to make daemon softwares. Just use softwares that allow you to run headless and make a shortcut that runs the exe with a flag.
# Task Anatomy
### Triggers
Whatever triggers the program to run, whether it is scheduled or requires an action
### Actions
Steps that define how programs are run and when programs are run
### Conditions
Extra criteria that must be met for the program to run:
- Is system idle?
- Is system connected to internet?
# Creating A Task
1. 
 ![[Syncthing-20240303214921118.webp]]
2.  
![[Syncthing-20240303214845050.webp]]
3. Allow the task to be ran automatically when user logs in
![[Syncthing-20240303215613721.webp|441]]
4. The arguments will depend on the program you are running
![[Syncthing-20240303215509457.webp|514]]
5. In the settings, uncheck the stop task after ...
![[Syncthing-20240303215729275.webp|498]]
# Deleting A Task
Open command prompt in administrator mode and type in:
`schtasks /Delete /TN "<task name>" /F`
