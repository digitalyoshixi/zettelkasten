---
tags:
  - web
  - security
aliases:
  - Cache Deception
---
Tricking a [[Cache Server]] into storing sensitive user data so that attackers can access it later.
# Identification
- Test endpoints that support `GET`, `HEAD`, `OPTIONS`
- Identify discrepancies in how cache and origin servers parse the URL path
	- Map URL to resources
	- Process delimiters
	- Normalize paths
- Craft malicious URLs that abuse this discrepancy
# Tools
- [[Param Miner]]