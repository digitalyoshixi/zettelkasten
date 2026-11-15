---
tags:
  - windows
---
```
ldapwhoami -x -H ldap://$DCIP -D $USER"@"$DOMAIN -w $USERPASS
```
# Turn on Binds