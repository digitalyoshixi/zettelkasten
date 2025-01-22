---
tags:
  - IT
  - security
---
[[eXtensive Markup Language|XML]] files used for the configuration of security policies for certain users and groups.
These policies may be:
- [[Mobile Application Management|MAM]]
- VPN access
- Network access
- Access to employee's files (Depends on implemented privacy policy)
![[Mobile Device Management Policies-20240724185152763.webp|535]]
Profiles can be different depending on the group. i.e product managers have higher permissions.
Several XML files can be applied to one user and may end up conflicting in permissions.
The [[Mobile Device Management Policies|MDM]] server must be responsible for handling these conflicts.