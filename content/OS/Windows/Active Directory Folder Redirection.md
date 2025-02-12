---
tags:
  - active_directory
  - windows
---
Setting up folders on a user's active directory account to replace the local folders in their current windows machine.
# Redirect
[[Windows Group Policy Management Console|gpmc.msc]] > OU > Right Click >  Create GPO in this domain and then create the policy> Right Click new policy > Edit > User Configuration > Policies > Folder Redirection 
![[Active Directory Folder Redirection-20240821160711169.webp]]
Right click folder > Properties > Setting > Basic - redirect everyones folder to the same location > Set Root Path
![[Active Directory Folder Redirection-20240821160826046.webp]]
[[Windows gpupdate]] on affected devices