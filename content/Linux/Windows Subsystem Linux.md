---
tags:
  - windows
  - linux
aliases:
  - WSL
  - Subsystem
---
This is a method to use linux comandline on a windows device. windows uses ubuntu command line which is debian, which is arguably the best terminal set we can get. 
Windows provides official support for this: https://learn.microsoft.com/en-us/windows/wsl/install
## Installation
To install this, you just need powershell and an administrator account.
![[Pasted image 20230909205644.png]]
then simply type the command:
`wsl --install`
Restart the computer.
Then, go to "Turn Windows Features On or Off"
And enable the following features:
![[Pasted image 20230910154644.png]]
Restart the computer again.
Open Ubuntu
![[Pasted image 20230910154714.png]]
And then make your linux user.
![[Pasted image 20230910154736.png]]
Now you can use Ubuntu commands
## Multiple Distros
You are not limited to debian-based commands. You may also want to use void or arch commands.
To see all installed distros, type: `wsl -l`
![[Pasted image 20230910155436.png]]
If you want arch, it is going to be a hassle: 
https://blog.depau.eu/2020/03/05/installing-arch-wsl-manually/
