---
tags:
  - security
---
A protocol used to secure existing [[Domain Name Server|DNS]] traffic. 
Runs on `tcp/53` or `udp/53`
Ensures each DNS packet is signed, creating a [[RRSIG]] record to prevent against attacks.
Prevents [[DNS Cache Poisoning]]