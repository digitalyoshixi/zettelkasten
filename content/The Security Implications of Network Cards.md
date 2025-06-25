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
- Theoretical exploit chain:
	- B