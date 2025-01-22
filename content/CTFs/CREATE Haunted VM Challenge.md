---
tags:
  - ctf
---
# Recon
The initial challenge is laid out like such:
![[CREATE Haunted VM Challenge-20241030205744667.webp|486]]
### Hint Level 5
Typing `vim` has this hint:
![[CREATE Haunted VM Challenge-20241030205855887.webp|480]]

### Hint level 3
This is the output for `cat /etc/passwd`. 
![[CREATE Haunted VM Challenge-20241030210116252.webp]]
I can `sudo passwd` to change my root password and `sudo passwd create` to change my local user's password
![[CREATE Haunted VM Challenge-20241030172151106.webp]]
### Hint level 2
![[CREATE Haunted VM Challenge-20241030175005548.webp]]