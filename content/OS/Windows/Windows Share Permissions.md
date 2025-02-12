---
tags:
  - windows
---
Permissions for network shares through [[Windows net|net]]. 
These permissions apply only to network users and not the local computer user themselves.
Share permissions are **rarely modified**. Most of the time it is [[New Technology File System|NTFS]] permissions that will be modified instead.
# NTFS Permission Priority
[[NTFS Permissions]] that are **more restrictive** overwrite share permissions.
Example:
- Share permission allows full control
- Local NTFS allows read only
Since the NTFS permission is more restrictive, then the remote access permissions would be read-only rather than full control.