---
tags:
  - security
---
 A [[Active Directory Certificate Services|ADCS]] [[Privilege Escalation]] vulnerability.
 Caused by improperly configured [[Access Control Model|ACL]] on [[AD Configuration Naming Context]].
# Attack
- Improper ACL on some [[AD Configuration Naming Context|NC]] (`CN=Public Key Services`, `CN=Services`, `CN=Cnfiguration`, `DC=...`) allows `Write` permissions (`WriteDACL, WriteOwner, WriteProperty, FullControl`)
- Attacker adds a new attacker-controlled cert here