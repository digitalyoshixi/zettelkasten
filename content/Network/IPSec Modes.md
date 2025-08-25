---
tags:
  - networking
aliases:
  - Tunnel Mode
  - Always-on-Mode
  - Transport Mode
---
# Tunnel Mode
Mode wherein user creates VPN session from a remote location.
During tunnel mode, [[Authentication Header|AH]] and [[Encapsulating Security Payload|ESP]] are both encrypted.

Requires pre-shared keys and certificates through [[Kerberos]].
# Always-on Mode
Applied to establish long-term connections between two sites.
- [[Authentication Header|AH]] and [[Encapsulating Security Payload|ESP]] are always encrypted
# Transport Mode
Used during creating of IPSec tunnel.
- Only [[Encapsulating Security Payload|ESP]] in encrypted.