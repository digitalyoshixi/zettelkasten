---
tags:
  - security
aliases:
  - NTML Relay to AD CS RPC Interface
---
A [[Privilege Escalation]] on [[Active Directory Certificate Services|ADCS]] that involves a [[NTLM Relay]] to a [[ADCS RPC Interface]].
The [[ADCS RPC Interface]] does not have protection against [[Man-In-The-Middle|MITM]] attacks.
# Requirements
- [[Active Directory Certificate Services|ADCS]] using [[ADCS RPC Interface]]
# Attack
- Attacker sets up a NTLM relay tool
- Attacker coerces privileged account with [[PetitPotam]]
- Relay this authentication request back to RPC endpoint
- Retrieve certificate and use for privileged access
# Identification
Use [[certipy]] look for:
- `Enforce Encryption for Requests : Disabled`