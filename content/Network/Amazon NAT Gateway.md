---
tags:
  - networking
  - cloud
---
A egress gateway to reach the internet.
- Used to expose [[AWS Virtual Private Cloud|AWS VPC Private Subnets]] to the internet
- Never accepts inbound communication from internet
- Only accepts outbound communication originating from VPC
# Route Table
![[Amazon NAT Gateway-1788878176665.webp]]
- Any 0.0.0.0 traffic will be routed to the NAT gateway