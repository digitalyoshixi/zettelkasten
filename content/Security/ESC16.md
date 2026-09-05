---
tags:
  - security
  - windows
aliases:
  - Security Extension Disabled on CA
---
A [[Privilege Escalation]] in [[Active Directory Certificate Services|ADCS]]. The CA is configured not to include [[Security Identifer|SID]] security extension in any issued certificates. Certificate identification falls back on other methods like [[Subject Alternative Name Certificate|SAN]]
# Requirements
- `szOID_NTDS_CA_SECURITY_EXT` ([[Object Identifier|OID]] `1.3.6.1.4.1.311.25.2`) is disabled
- 
