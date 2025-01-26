---
tags:
  - networking
aliases:
  - RADIUS
---
Protocol for implementing [[Authentication, Authorization, Accounting|AAA]]. It centralizes authentication, authorization and auditing.
It:
- Is primarily for network access
	- [[Virtual Private Network|VPN]] access
	- Router, Switch, Firewall access
	- Server authentication
	- [[WI-FI|IEE 802.11]] network access
- Combines authentication and authorization
- Encrypts only the password in the access-request packet
Completely open protocol, that is partially encrypted and communicates over `udp/1812` and `udp/1813`.
