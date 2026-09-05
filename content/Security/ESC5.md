---
tags:
  - security
aliases:
  - Vulnerable PKI Object Access Control
---
 A [[Active Directory Certificate Services|ADCS]] [[Privilege Escalation]] vulnerability.
 Caused by improperly configured [[Access Control Model|ACL]] on [[AD Configuration Naming Context]].
# Requirement
- Improper ACL on some [[AD Configuration Naming Context|NC]] (`CN=Public Key Services`, `CN=Services`, `CN=Cnfiguration`, `DC=...`) allows `Write` permissions (`WriteDACL, WriteOwner, WriteProperty, FullControl`)
- Attacker does any of the following:
	- Attacker modifies `CN=NTAuthCertificates` and adds a new attacker-controlled cert here
	- Attacker alters [[Authority Information Access|AIA]] or [[CRL Distribution Point|CDP]] paths to redirect certificate validation, could lead to [[Denial of Service|DoS]]
	- Attacker alters weak objects that configure [[Object Identifier|OID]] policies, [[Active Directory Enrollment Agent]] restrictions, etc
# Identification
- [[Bloodhound]] with data collection that includes ACL
- [[Powershell]] with [[Windows Active Directory|AD]] cmdlets like `Get-Acl` and `GetAdObject`
- Using [[ADSIEdit.msc]] or [[ldp.exe]]
# Exploitation
- Use powershell with `Set-AdObject` or `Set-Acl`
- Use [[ADSIEdit.msc]] or [[ldp.exe]]