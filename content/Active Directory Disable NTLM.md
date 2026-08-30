---
tags:
  - windows
  - security
---
1. Open [[Windows Group Policy Management Console|gpmc.msc]], right click to edit default domain controllers policy
![[Active Directory Disable NTLM-20260830191803207.webp]]
2. Group policy editor, navigate to `Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options > Network Security: Restrict NTLM: NTLM Authentication in this domain`
![[Active Directory Disable NTLM-20260830191853652.webp]]
3. Properties, Define policy setting to be deny all
4. `gpupdate /force`