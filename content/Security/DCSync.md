---
tags:
  - security
  - windows
---
An attack against [[Windows Active Directory|Active Directory]] wherein an attacker can simulate behavior of a [[Domain Controller]] to replicate the domain and use that copy to extract password hashes.
Uses [[Microsoft Directory Replication Service Remote|MS-DRSR]]
Used by [[mimikatz]] to extract password hashes.
Can lead to a [[Golden Ticket Attack]]
# Attack
1. An account with the following permissions is compromised
	1. [[Domain Admin]]
	2. System account with delegation permissions
	3. Account with "DS-Replication-Get-Changes" and "DS-Replication-Get-Changes-All" rights
2. Craft request as if you were a legitimate DC participating in replication, send through `DRSUAPI` `GetNCChanges` function
3. DC responds with
	- NTLM hashes
	- Kerberos keys
	- KRBTGT account hash