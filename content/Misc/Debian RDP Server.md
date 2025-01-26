---
tags:
  - projects
  - debian
  - networking
---
So, we have downloaded a fresh debian 12. no desktop environment, just system utils and the bare bones machine is alive
# Grimy Shit
For some reason, sudo isnt installed by default.
1. `su -`
2. `apt-get install sudo -y`
3. `usermod -aG sudo yourusername`

# AwesomeWM
- Go get your graphical interface
[[Awesome WM]]
`sudo apt-get install awesome`
`sudo apt-get install xorg`
change the rc.lua config file to have a symbolic link
`mkdir ~/.config/awesome`
`sudo link /etc/xdg/awesome/rc.lua ~/.config/awesome/rc.lua`
`sudo chown myusername ~/.config/awesome/rc.lua`
# XRDP
`sudo apt-get install xrdp -y`
check if it worked
`sudo systemctl status xrdp`
add their certificate
`sudo adduser xrdp ssl-cert`
### Firewall
`sudo apt-get ufw`
`sudo ufw allow 3389/tcp`
`sudo ufw reload`

# Get IP and RDP in
`ip a`
get that ip address

# Connect to Wifi
[[nmcli]]
OR
on a windows machine, if you want network profiles, run the command:
1. `netsh wlan show profiles`
2. `netsh wlan export profile THENETWORKNAME`

# Add Friends
if you try on multiple devices to RDP on the system on the same account, one of the devices will be booted.
We must each connect on different accounts
lets make those different accounts.
