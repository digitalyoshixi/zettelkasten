---
tags:
  - windows
aliases:
  - NTLM
---
A suite of network protocols developed for [[Windows NT 4.0]].
Often used for [[Authentication]] during:
- [[Windows Domain]] joining
- Auth between AD forests
- Auth between computers that dont run Windows OS
- Auth to computers not inside the domain
Vulnerable to [[Pass The Hash Attack]]. 
# Concepts
- [[Local Security Authority Subsystem Service|LSASS]] 
### Auth
- [[LAN Manager]]
- [[NTLMv1]]
- [[NTLMv2]]
# Attacks
- [[NTLMv1 Downgrade Attack]]