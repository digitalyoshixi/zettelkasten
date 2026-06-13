---
tags:
  - networking
---
The cisco operating system for its switches. Replaced [[CatOS]]
# Concepts
- [[Cisco IOS Hardening]]
- [[Cisco IOS Quality Of Life Configuration]]
- [[Cisco User Levels]]
# Modes
![[Cisco IOS-20260606160715628.webp]]
### Configuration Submodes
![[Cisco IOS-20260606161358730.webp]]
- Interface mode : modify [[Network Interface]]
- VLAN mode: modify VLANs
- Console line mode: modify console
- VTY line more: Modify VTY
![[Cisco IOS-20260606161229825.webp]]
### User Exec Mode
- User can look around
- User can't break things
### Privilege Enable Mode
- Enter via `enable` command
- Exit via `disable` command
- Can trigger reboots, shut downs
### Configure Mode
- Enter via `configure` from enable mode
- Exit via `end`
# Viewing Config
```
show running-config
```
# Help Commands
- `?` Help for all commands
- `command?` Help for specific command
# Viewing Mac Address
```
show mac address-table dynamic
```
# Live-Viewing Mac Address
```
debug mac address-table dynamic
```
# Entering Global Configuration Mode
```
configure terminal
```
# Configure Switch Name
```
hostname Daniel
```
# Entering Context-Setting Submode
```
line console 0
```
# Configure Simple Password
```
password hope
```
# View [[Content Addressable Memory Table|CAM Table]]
```
show mac address-table dynamic
```
```
show mac address-table dynamic address 0200.1111.1111
```
```
show mac address-table dynamic interface fastEthernet 0/1
```
```
show mac address-table dynamic interface vlan 1
```
# Clearing [[Content Addressable Memory Table|CAM Table]]
```
clear mac address table dynamic
```
```
clear mac address table vlan <vlan-number>
```
```
clear mac address table interface <interface-id>
```
```
clear mac address table address <mac-address>
```
# Show Interfaces
```
show interfaces status
```
# Show SSH Info
```
show ip ssh
```
```
show ssh
```
# Verifying IPv4
```
show dhcp lease
```
```
show interfaces vlan 1
```
```
show ip default-gateway
```
# Showing History
```
show history
```
# Modify History Size
```
history  size <x>
```
# Set Console Logging
```
no logging console
```
```
logging console
```
# Set Synchronized Logging
These will display logs during `show` command
```
logging synchronous
```
# Disable Default Domain Lookup
```
no ip domain-lookup
```