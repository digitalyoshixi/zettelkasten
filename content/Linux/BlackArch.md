---
tags:
  - arch
  - redteam
---
THE BEST linux distribution for HACKING
# Installation
https://www.youtube.com/watch?v=zHDzfjuihi0 
https://www.blackarch.org/downloads.html 
Download the full blackarch ISO.
Ensure that it has atleast 100GB of storage, and beef it up with good RAM.
you have access to the `root` user. password is `blackarch`
### Network Access
`dhcpcd`
`ifconfig`
and then `pacman -Sy`
dont do a system upgrade yet.
### Blackarchinstall
`blackarch-install`
you know how to do this part

### Speed boost - Virtualbox Guest Additions
`sudo pacman -Sy virtualbox-guest-utils`

### Remove java conflicts and system upgrade
`sudo pacman -Rdd jre-openjdk-headless`
`sudo pacman -Rdd jre-openjdk`
`sudo pacman -Syu`

This repo is a giant bloated dog shit. Just use regular arch and install all you need on it

# Arch Linux Include BlackArch Repository
If you don't want the entirety of blackarch, you can use your regular arch distribution and download the tools from the blackarch repo.
### Installation
`curl -O https://blackarch.org/strap.sh`
This will download a strap.sh on your local computer.
`chmod +x strap.sh`
`sudo ./strap.sh`

You can now install from the blackarch repo.
`sudo pacman -S dirbuster`