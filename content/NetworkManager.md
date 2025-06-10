---
tags:
  - linux
  - networking
---
This is the network package for all linux distributions that comes default.
# Service
1. `sudo systemctl enable NetworkManager`
2. `sudo systemctl restart NetworkManager`
# Configuration
1. `vim /etc/network/interfaces`
```
auto lo
iface lo inet loopback

iface eth0 inet static
  address 192.168.1.5
  netmask 255.255.255.0
  gateway 192.168.1.254
  dns-nameservers 192.168.1.250
 
```