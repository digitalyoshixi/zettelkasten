---
tags:
  - networking
aliases:
  - RADIUS
---
Protocol for implementing [[Authentication, Authorization, Accounting|AAA]]. It centralizes authentication, authorization and auditing.
Uses [[Shared Secret]]
It:
- Is primarily for network access
	- [[Virtual Private Network|VPN]] access
	- Router, Switch, Firewall access
	- Server authentication
	- [[WI-FI|IEE 802.11]] network access
- Combines authentication and authorization
Completely open protocol, that is partially encrypted and communicates over `udp/1812` and `udp/1813`.
# Protocol
1. Requests for password
2. Only password is encrypted in access-request packet
