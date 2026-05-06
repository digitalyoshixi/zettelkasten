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
![[Windows Active Directory-20240717215817738.webp]]
The active directory can be configured here.
- Built-in: All domain groups are stored like users and administrators
- Computers: All systems in the network
- Domain Controllers: Usually just 1 which is the Active Directory server
- Users: All added users into the domain. Group policies created here will supersede [[Windows Local Security Policy]].
# Removing User
Active Directory > Right click on the correct system > Properties > Member Of > Remove user
![[Windows Active Directory-20240718011622483.webp|549]]
# User Properties
![[Windows Active Directory-20240718021458509.webp|430]]
In the Users tab, right clicking the properties of a User, you can:
- Create [[Visual Basic]] scripts to run at login
- Set home folders like Documents, Downloads, etc
- Redirect home folder locations to that found on the server, so that when the user logs in to a new computer, they will still have their old files
# Concepts
- [[Organizational Unit|OU]]
- [[Active Directory Login Scripts]]
- [[Active Directory Home Folder]]
- [[Active Directory Folder Redirection]]
- [[Windows Group Policies]]
- [[Windows Group Policy Management Console|gpmc.msc]]
- [[Active Directory Domain Services|AD DS]]
- [[X500 Format]]
- [[Updated Sequence Number|USN]]
- [[Security Identifer]]
- [[ADSI Edit]]
- [[Distinguished Name|DN]]
- [[Relative Distinguished Name]]
# [[Active Directory Security]]