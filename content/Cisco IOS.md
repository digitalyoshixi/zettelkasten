---
tags:
  - networking
---
The cisco operating system for its switches. Replaced [[CatOS]]
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