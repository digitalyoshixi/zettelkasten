---
tags:
  - networking
---
# No Internet Connectivity
1. Try [[Hyper Text Transfer Protocol|HTTP]] or [[Hyper Text Transfer Protocol Secure|HTTPS]]
2. [[ping]] loopback address or local IP address to see if protocol is working
3. [[ping]] [[Default Gateway]]
4. If the DNS is the problem, `ipconfig /flushdns` to reset dns cache on [[IT/Windows]]
5. [[Windows Settings]] > Network & Internet > Status > Troubleshooter
   ![[Internet Troubleshooting-20240723040836602.webp|494]]
5. Switch DNS servers. Try `8.8.8.8` or `1.1.1.1`
# No DHCP Server
1. Restart [[Router]]
2. Setup [[Network Interface Controller|NIC]] statically
# Local Connectivity but No Internet
1. Ping [[Router]] gateway
2. Ping [[Router]]'s WAN port (look at the router's manual for this)
3. Renew DHCP by holding down a button
4. Call [[Internet Service Provider|ISP]]
# Slow Network Speeds
1. `netstat` and view the foreign addresses that are being connected to. It is likely that one of these connections is slowing the rest of the network
   ![[Internet Troubleshooting-20240723041523785.webp]]
2. Enable Quality of Service in your router's web configuration to limit bandwidth or to prioritize certain users more than others
# Checking Latency
`ping` and then check the average round trip time
![[Internet Troubleshooting-20240723041853831.webp|472]]
# Poor Quality VoIP Calls
- Check for jitter (time between network frames)
- Check if network is congested
- Check if Quality of Service is enabled