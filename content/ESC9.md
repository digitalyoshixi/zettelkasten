---
tags:
  - security
  - windows
aliases:
  - No Security Extension on Template
---
A [[Active Directory Certificate Services|ADCS]] [[Privilege Escalation]] vulnerability.
A [[Active Directory Certificate Template|AD Certificate Template]] is not configured to include [[Security Identifer|SID]] security extension with the property `szOID_NTDS_CA_SECURITY_EXT` (OID `1.3.6.1.4.1.311.25.2`)
# Requirements
- Template configured to reject [[Security Identifer|SID]] with option `msPKI-Enrollment-Flag=CT_FLAG_NO_SECURITY_EXTENSION`
- [[Domain Controller]] certificate binding mode is 1 or 0 to enable fall-back to [[Subject Alternative Name Certificate|SAN]] or [[Domain Name Server|DNS]] names
- [[Extended Key Usage|EKU]] must allow for client authentication
- Attacker must be able to enroll this template
# Exploitation
