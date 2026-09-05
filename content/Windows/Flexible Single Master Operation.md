---
tags:
  - windows
aliases:
  - FSMO
---
Roles that can be distributed to a [[Domain Controller|DC]] that can help with performance and redundancy if one [[Domain Controller|DC]] goes down. The alternate DC will take over the missing role.
# Roles
- Schema master role: managed read-write copy of [[Active Directory Schema]]
- Domain naming master: makes sure dont create a second domain with same name in [[Active Directory Forest|AD Forest]]
- RID master: In charge of [[Security Identifer|SID]] for each object
- PDC emulator: The authoritative [[Domain Controller|DC]] in the domain responsible for authentication
- Infrastructure master role: Manages relationship of [[Globally Unique Identifier|GUID]], [[Security Identifer|SID]], [[Distinguished Name|DN]] between [[Windows Domain|Domains]]