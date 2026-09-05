---
tags:
  - networking
---
# Create VLAN
```
configure terminal
	vlan <vlan-id>
		name <name>
		exit
```
# Setup Interfaces
For a given interface:
```
configure terminal
	interface type number
		switchport acces vlan id-number
		switchport mode access
		end
```
# Show VLANs
```
show vlan brief
```
# Disable [[VLAN Trunking Protocol|VTP]]
```
vtp mode off
```
#  [[VLAN Trunking Protocol|VTP]] Transparent
```
vtp mode transparent
```
# Trunking Modes
```
switchport mode
```
Modes are:
- `access` : Always act as non-trunk port
- `trunk` : Always act as trunk port
- `dynamic desirable`: initiate negotation to choose whether to start using trunking
- `dynamic auto`: Wait to receive trunk negotiation messages
![[Cisco IOS VLAN Configuration-20260704180042379.webp]]