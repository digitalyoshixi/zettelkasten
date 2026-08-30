---
tags:
  - windows
  - security
---
1. Open [[Windows Group Policy Management Console|gpmc.msc]], right click to edit default domain controllers policy
![[Active Directory Disable NTLM-20260830191803207.webp]]
2. Group policy editor, navigate to `Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options`
![[Active Directory Disable NTLM-20260830191853652.webp]]
3. Toggle `Network Security: Restrict NTLM: NTLM Authentication in this domain` to `Deny All`
4. Toggle `Network Security: Restrict NTLM: Incoming NTLM Traffic` to `Deny All`
5. `gpupdate /force`
# Testing
Should fail:
```
nxc ldap $DCIP -u $USER -p $USERPASS --port 636 -d catbird.local  
```
Should succeed:
```
nxc ldap $DCIP -u $USER -p $USERPASS --port 636 -d catbird.local -k
```