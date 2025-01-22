---
tags:
  - windows
  - linux
---
Command to view all processes and their information
`ps aux`
![[Windows ps-20240715173746720.webp]]
# Commands
### `ps`
View all user processes
### `ps -e`
View all processes
### `ps aux`
viewing user processes with auxiliary information
# Fields
### USER
Who is running this process
### PID
[[Process|PID]] of the process
### %CPU
How much of the CPU this process is using
### %MEM
How much of the RAM this process is using
### VSZ
Total paged memory in KB
### RSS
Total physical memory in KB
### STAT
S: Waiting
R: Running
1: multithreaded
+:  foreground process
### START
When the process was started
### TIME
How long the process has been running
### COMMAND
Name of executable created by this process
