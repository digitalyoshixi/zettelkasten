---
tags:
  - cloud
aliases:
  - AWS VPC
  - AWS VPC Subnets
---
A private cloud on [[Amazon Web Services|AWS]]' platform.
![[AWS Virtual Private Cloud-1788875967059.webp]]
# Subnets
![[AWS Virtual Private Cloud-1788876365596.webp]]
- A public subnet has a route table pointing to the internet
- A private subnet has a route table only for local subnet
### Reserved Addresses
- \*\.\*.\*.0 : Network address
- \*\.\*.\*.1 : AWS Routing address
- \*\.\*.\*.2 : AWS DNS address
- \*\.\*.\*.3 : AWS reserved
- \*\.\*.\*.255 : Broadcast
# Concepts
- [[Route Table]]
- [[Amazon VPC NACLs]]
- [[Amazon VPC Security Groups]]
- [[Amazon NAT Gateway]]