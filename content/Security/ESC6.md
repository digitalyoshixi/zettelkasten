---
tags:
  - security
aliases:
  - Allow SAN Specification via Request Attributes
---
 A [[Active Directory Certificate Services|ADCS]] [[Privilege Escalation]] vulnerability.
 Involves abusing the [[Certificate Authority|CA]] configuration `EDITF_ATTRIBUTESUBJECTALTNAME2` flag that allows using [[Subject Alternative Name Certificate|SAN]] in the [[Certificate Signing Request|CSR]].
 - `san:<type>=<value>`
The [[Subject Alternative Name Certificate|SAN]] will be used to bypass template-level restrictions.
# Identification
[[certipy]] `find` inspects CA config:
- `User Specified SAN : Enabled`
# Exploitation
Cannot exploit anything by itself but can be chained with [[ESC9]], [[ESC16]] where the [[Key Distribution Center|KDC]] falls-back on [[Subject Alternative Name Certificate|SAN]] to identify rather than [[Sin]].
1. Request certificate with malicious [[Subject Alternative Name Certificate|SAN]] (UPN and SID url)
2. Authenticate using the obtained certificate