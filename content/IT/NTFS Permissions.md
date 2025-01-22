---
tags:
  - windows
---
[[New Technology File System|NTFS]] has certain permissions set on who can read, write, delete, execute a file/folder.
NTFS permissions apply to both network and local users.
# Permissions
![[Pasted image 20240706153929.png]]
Full Permissions list can be found here: https://www.ntfs.com/ntfs-permissions-file-folder.htm
### Permission Hierarchy
More restrictive permissions are applied.
Explicit Deny > Explicit Allow > Inherited Deny > Inherited Allow
# Editing Permissions
![[NTFS Permissions-20240706195520317.webp|459]]
# Folder Permission Inheritance
![[NTFS Permissions-20240706200519839.webp]]
Subfolders inherit the same permissions as the parent folder.
### Explicit Permission
A child folder that has explicit NTFS permissions will ignore permission inheritance
![[NTFS Permissions-20240821204559491.webp|373]]
# File Permission Propagation
How permissions will change for a file moved or copied to a new directory
![[NTFS Permissions-20240706201057919.webp]]