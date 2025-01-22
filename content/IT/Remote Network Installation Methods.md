---
tags:
  - os
aliases:
  - Unattended Installations
  - Remote Network Installation
  - Image Deployment
---
# Installation Types
### Remote Network Installation
Installing an OS through an OS image stored on a server
![[Remote Network Installation-20240705013900028.webp]]
Usually you will find these on mirrors of the OS themselves. Like, [[Debian]] and [[Arch]] has alot of mirrors where you can just net install from.
### Unattended Installation
Remote Network installation, but after installing the OS, shell scripts may also be ran to ensure the correct software and configurations are set. 
These installations require a [[Answer File]] to note what scripts are ran after installation.
### Image Deployment
Storing an entire [[Disk Image]] including all the software and files on a server. You would use image cloning software like Norton Ghost to load these images into your drive.
![[Image Deployment-20240705014137196.webp]]
# Setup
1. Enable [[Preboot Execution Environment|PXE]] to allow for network installations
2. Change boot order priority to be network first
3. Reboot PC and press F12 at startup for network boot
   ![[Remote Network Installation Methods-20240705020755160.webp]]
