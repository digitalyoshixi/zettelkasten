---
tags:
  - networking
---
# Network Disconnect from Cable
When there is no network, run `ipconfig`/`ifconfig`. If there is an [[Automatic Private IP Addressing|APIPA]] address, then there is a clear disconnect between the device and the DHCP server.
### Solutions
1. Check [[RJ-45|Ethernet Cable]] connectivity
2. Check power in DHCP server
3. Check if [[Network Interface Controller|NIC]] is enabled in [[Windows Device Manager]]
# Link Light Connectivity
There may be a cable connection issue if the link-light does not have a stable green light and a flashing orange light. May be caused by:
- Bad port
- Bad Cable - Use a [[Cable Tester]]
- Bad [[Switch]]
This is called [[Port Flapping]]
# NIC Diagnostic
- Sometimes NIC driver installations come bundled with diagnostic software to check the NIC circuitry.
- Install a [[Loopback Plug]] which sees if it can receive data it sends towards itself.
  ![[LAN Troubleshooting-20240718023739893.webp]]
# Cable Testing
![[LAN Troubleshooting-20240718024335992.webp]]
Using a [[Time-Domain Reflectometer]] on a cable will tell you:
- Where the cables broke
- How far a length the cable is
Ensure you test with the cable unplugged from both ends and a loopback device on the opposite end
# Cable Tracing
If a setup has multiple cables, that it is too hard to trace its cause, then use a toner generator and toner probe.
![[LAN Troubleshooting-20240718024728982.webp|389]]
1. Place the toner generator at one end of the cable
2. When the toner probe is touching the cable with the toner generator on the other side, it will make a sound
# Can't Ping [[Default Gateway]]
- The router is down
# [[Point-to-point Communication|Duplex]] Mismatch
The network devices configured at different duplex versions. 
It will cause slower network communication.