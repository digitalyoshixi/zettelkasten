---
tags:
  - security
  - windows
---
A [[Authentication Coercion|NTLM Relay Attack]] designed to use the same [[Local Security Authority Subsystem Service|lsass.exe]] authorization session to escalate priviledges.
1. User initiates auth session with lsass
2. LSASS runs in local auth so it can send a SYSTEM token
3. Uses [[NTLM Relay]] to send the SYSTEM token to a C2 or [[Repeater]]
4. Repeater sends SYSTEM token back to lsass so local user becomes elevated
# Uses
- [[NTLM Not Dead]]
