---
tags:
  - windows
---
Accessible panel through [[Windows Control Panel]].
Allows configuration of:
- Network adapters 
- Network shares
- Streaming options
- Network connections
# Adjusting Half Duplex Speed
1. Change adapter settings
   ![[Windows Adjusting Half Duplex Speed-20240717200412316.webp]]
2. Right click the [[Network Interface Controller|NIC]] and enter properties
   ![[Windows Adjusting Half Duplex Speed-20240717201108092.webp|399]]
3. Configure > Advanced > Speed & Duplex
   ![[Windows Adjusting Half Duplex Speed-20240717201157165.webp|607]]
4. Adjust the value accordingly
# Enabling [[Network Interface Controller|Wake-on-LAN]]
Change Adapter Settings > Right click [[Network Interface Controller|NIC]] and Properties > Configure > Power Management > Allow this device to wake the computer
![[Network and Sharing Center-20240717202538733.webp]]
# Enabling [[Quality of Service|QoS]]
Change Adapter Settings > Right click [[Network Interface Controller|NIC]] and Properties > Configure > Advanced > Priority & VLAN > Priority & VLAN Enabled
![[Network and Sharing Center-20240717202840379.webp|530]]