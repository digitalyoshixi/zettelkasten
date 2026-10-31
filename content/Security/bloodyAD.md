---
tags:
  - security
---
A swiss army knife tool for active directory
# Add new DNS Record
```
bloodyAD -H $DCIP -d $DOMAIN -u $USER -p $USERPASS add dnsRecord <name> <ip_address>
```