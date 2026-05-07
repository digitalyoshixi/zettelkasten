---
tags:
  - windows
  - security
aliases:
  - Any Purpose Certificate Template
---
An attack against [[Active Directory Certificate Services]] that can cause [[Privilege Escalation]].
Involves [[Active Directory Certificate Template|AD Certificate Template]] that have Any Purpose [[Extended Key Usage|EKU]] to be used to create certificates of [[Domain Administrator]] accounts.
# Requirements
- Requires there being a 'Any Purpose' [[Extended Key Usage|EKU]] ([[Object Identifier|OID]] 2.5.29.37.0) or templates with no [[Extended Key Usage|EKU]] specified at all.
- Requires low-privileged users to be able to enroll these templates
# Finding with [[certipy]]
Use [[certipy]] `find` and look for:
- `ESC2: Template can be used for any purpose`
- `ESC2: Template has Certificate Request Agent EKU set`
- `ESC2 Target Template : Template can be targetted as part of ESC2 exploitation or ESC3 Target Template`
- `Any Purpose : True`
# Exploitation
1. Request the Any Purpose certificate for the attacker
2. Request a administrator certificate for the attacker using the Any Purpose certificate
3. Authenticate on behalf of the cert returned