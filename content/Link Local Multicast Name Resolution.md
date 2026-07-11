---
tags:
  - security
aliases:
  - LLMNR
---
A protocol based off [[Domain Name Server|DNS]] to allow name resolution for hosts on the same local link.
- If there is no DNS record found, will broadcast a request to ask entire network for the corresponding host
Used commonly in [[Windows Active Directory|AD]] environments for host discovery.
# Vulnerabilities
- [[LLMNR Poisoning]]