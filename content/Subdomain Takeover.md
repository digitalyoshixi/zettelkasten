---
tags:
  - security
---
An attack that involves an attacker gaining control over a [[Domain Name]] of a target domain.
Happens if there is a [[Canonical Name|CNAME]] record in DNS but no host is providing content
# Tools
- [[subfinder]]
- [[sublist3r]]
- https://crt.sh
- [[theHarvester]]
# Process
1. Find subdomains with subfinder
2. Run all subdomains through [[nslookup]] to get CNAME
3. Check if any CNAMEs can be taken over https://github.com/EdOverflow/can-i-take-over-xyz