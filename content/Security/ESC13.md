---
tags:
  - security
  - windows
aliases:
  - Issuance Policy with Privileged Group Linked
---
A [[ADCS Privilege Escalation]] attack that occurs when a [[Active Directory Certificate Template|AD Certificate Template]] is setup with 'Issuance Policy' linking it to a specific user group.
- [[Key Distribution Center|KDC]] automatically assumes permissions of those specific user groups with the cert
# Requirements
- Certificate template has one or more issuance policy to a privileged group's [[Object Identifier|OID]]
- [[Object Identifier|OID]] must exist in [[Windows Active Directory|AD]]
- Cert template must allow for client authentication
- Low priviledge user must have ability to enroll this certificate
# Identification
[[certipy]] `find`;
- `Issuance Policies : ...`
- `Linked Groups : ...`
# Attack
1. Request certification with [[certipy]]
2. Authenticate with the certification