---
tags:
  - windows
  - os
aliases:
  - Active Directory Domain
  - Domain
---
Only available for [[Windows Server]] editions.
It is a [[Server]] with a [[Domain Name]] (e.g activedirectoryserver.com) that stores:
- Users
- Groups
- Computers & Devices
- Other objects
All local computers can be logged into with the users stored in the domain server.
It aims to secure data.
![[Windows Domains-20240704220913655.webp]]
# Joining A Domain
Settings > About PC > Rename this PC (Advanced) > Computer Name > Change > Input the domain you want to join
# Domain Users
Logging into a domain will require the username be in the form of:
`<Domainname>\<Username>`