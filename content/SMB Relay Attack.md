---
tags:
  - security
---
A [[Man-In-The-Middle]] attack that uses [[Server Message Block Protocol|SMB]] relay.
Used to capture password hashes.
# Attack with [[NTLM Relay]]
### Requirements
1. A computer without SMB signing
2. Another computer without SMB signing that the first computer has a user account on
### Process
1. Setup [[responder]] to poison SMB requests
2. Setup [[ntlmrelayx]] to read requests of responder and send them to second computer
3. Use [[Netexec|nxc]] [[PetitPotam]] to coerce first computer
4. ntlmrelayx will recieve the authentication response from the second computer if the first computer has an actual account
# Alternate Process with [[NTLM Reflection]]
1. Using [[NTLM Not Dead|CVE-2025-33073]], you can self-reflect without a second computer
# Mitigations
- Implement [[UNC Hardening]]