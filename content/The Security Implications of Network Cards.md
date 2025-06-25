---
tags:
  - security
---
# Notes:
- Your [[Network Interface Card]] is a computer. 
- The issue is with [[Peripheral Component Interconnect Express|PCIe]] direct memory aces. can directly write to [[Random Access Memory|RAM]]
- You can exploit hardware, firmware vulnerabilities
- We can tell by:
	- NMIC
	- Firmware verification ([[fwupd]])
- We dont see these attacks because nobody is looking if the firmware of your network card changes
- These attacks are very advanced and hardware dependent
- Direct memory access through PCIE. It is possible to perform these from:
	- [[Network Interface Controller|NIC]]
	- [[Graphics Card|GPU]]
- If you have [[Wake-on-LAN]], you can exploit an entire network remotely. Many chipset manufacturers or government agencies will be able to take over your entire network
  ![[The Security Implications of Network Cards-20250625222725525.webp]]
- Theoretical exploit chain:
	- Be the US government
	- Contract local network card chipset manufacturers
	- Mix hardware and software vulnerabilities
	- In network card memory exploits done ove the network
	- bypass OS level detection with PCIE point-to-point between network cards. Take over entire network
	- Compromise private keys or sensitive data with writes to arbitrary locations in RAM
	- Interface with UEFI/Bios to compromise other hardware
- Wireless is vulnerable
	- [[Cellular Data]]
	- [[WI-FI|WIFI]]
	- [[Bluetooth]]
- Solution is to make this problem more visible, and make these exploits open source
- ![[The Security Implications of Network Cards-20250625222604351.webp]]
  The northbridge and the southbridge should seperate PCI components. Adding something to filter between them is vital
- https://www.computerworld.com/article/1509757/jedi-packet-trick-punches-holes-in-firewalls.html