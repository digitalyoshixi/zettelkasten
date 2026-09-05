---
tags:
  - security
  - windows
---
A [[Active Directory Certificate Services|ADCS]] [[Privilege Escalation]] attack that abuses weak cert mapping for [[Microsoft Secure Channel]].
# Requirements
- Registry key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\CertificateMappingMethods` configured to allow [[User Principal Name]]-based mapping (has a bit-flag multiple of `0x4`, so `0x4, 0xC, 0x1C, 0x1F,...`)
# Exploit
1. Attacker modifies [[User Principal Name|UPN]] through modifying the object that has a `GenericWrite` or `WriteProperty` permission to a administrator's [[User Principal Name|UPN]]
2. Uses target account to enroll for client authentication certificate
3. Attacker reverts UPN covering their tracks
4. Attacker authenticates with the certificate via [[Microsoft Secure Channel|Schannel]] to a service
# Identification
- Must check registry for `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\CertificateMappingMethods` on each relevant server 