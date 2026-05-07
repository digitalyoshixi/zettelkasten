---
tags:
  - windows
  - active_directory
aliases:
  - Active Directory
  - AD
---
A live directory service which functions similarly to a [[Windows Domain]] in the fact that it:
- Stores domain user login credentials
It expounds on this by also storing:
- Printer information
- Computer names
- Location information
- Group policies
- Encryption keys
Active directory is powered by [[Lightweight Directory Access Protocol|LDAP]] on `tcp/389`
# Active Directory Users and Computers
The active directory can be configured here.
- Built-in: All domain groups are stored like users and administrators
- Computers: All systems in the network
- Domain Controllers: Usually just 1 which is the Active Directory server
- Users: All added users into the domain. Group policies created here will supersede [[Windows Local Security Policy]].
# Removing User
Active Directory > Right click on the correct system > Properties > Member Of > Remove user
# User Properties
In the Users tab, right clicking the properties of a User, you can:
- Create [[Visual Basic]] scripts to run at login
- Set home folders like Documents, Downloads, etc
- Redirect home folder locations to that found on the server, so that when the user logs in to a new computer, they will still have their old files
# Concepts
### Fundamental
- [[Windows Domain]]
- [[Active Directory Forest]]
- [[Domain Controller]]
- [[Active Directory Forest]]
- [[Organizational Unit|OU]]
- [[Global Catalog]]
- [[Active Directory Schema]]
- [[Security Identifer]]
- [[Distinguished Name|DN]]
- [[Relative Distinguished Name]]
- [[Active Directory Domain Services|AD DS]]
- [[Active Directory Site]]
- [[Kerberos]]
- [[Flexible Single Master Operation|FSMO]]
### Tools
- [[gporeport]]
- [[Windows Group Policy Management Console|gpmc.msc]]
- [[ADSI Edit]]
### Guides/Techniques
- [[Active Directory Login Scripts]]
- [[Active Directory Home Folder]]
- [[Active Directory Folder Redirection]]
- [[Windows Group Policies]]
- [[Active Directory Replication]]
### Misc
- [[Updated Sequence Number|USN]]
- [[X500 Format]]