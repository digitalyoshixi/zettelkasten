---
tags:
  - security
aliases:
  - Template Hijacking
---
A [[Privilege Escalation]] attack against [[Active Directory Certificate Services|ADCS]].
Caused by improper [[Access Control Model|ACL]] on [[Active Directory Certificate Template|AD Certificate Template]].
# Requirements
- Attacker gains permissions (`WriteOwner`, `Write`, `WriteDACL`) to modify a [[Active Directory Certificate Template|AD Certificate Template]] located at:
	- `CN=Cerificate Templates`
	- `CN=Public Key services`
	- `CN=Services`
	- `CN=Configuration`
# Identification with [[certipy]]
With [[certipy]] `find`:
- Look at certificate templates and [[Access Control Model|ACL]]
- `Full Control, Write Dacl, Write Owner` or other `Write Property` rights on attributes like:
	- `msPKI-Enrollment-Flag`
	- `msPKI-Certificate-Name-Flag`
	- `pKIExtendedKeyUsage`
	- `nTSecurityDescriptor`
# Attack
- Attacker modifies template with [[certipy]] `template`:
	- Grant enrollment rights of template to themselves or a broad group like "Domain Users"
	- Enable "Enrollee Supplies Subject" setting (`CT_FLAG_ENROLEE_SUPPLIES_SUBJECT`)
	- Add "Client Authentication" or "Any Purpose" [[Extended Key Usage|EKU]]
	- Remove security controls like "CA certificate manage approval"
- Attacker requests certificate using modified template
- Attacker authenticates with obtained certificate
- Attacker performs an alternative [[ADCS Privilege Escalation]] attack