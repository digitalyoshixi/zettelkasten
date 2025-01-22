---
tags:
  - networking
  - privacy
---
My school blocks VPNs. I require a VPN to stay private so I can log into my apps.
https://www.youtube.com/watch?v=FcT6i6k0m3w

The idea is, there are several ways this could happen.
1. IP blocking VPN servers
2. Domain blocking. block the VPN website so the App can't connect to the APIs
	1. VPNs set up [[Mirrors]] so that if one domain is blocked or down, use the other
3. Deep packet inspection
4. Port blocking. Blocks the usual suspects, PPTP, L2TP, SSTP, etc.
5. QoS(Quality of Service) filtering.  

