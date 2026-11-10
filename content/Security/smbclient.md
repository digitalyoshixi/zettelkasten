---
tags:
  - security
---
# Usage
```
smbclient //10.10.10.5/SYSVOL -U $USER --password=$USERPASS
```
# Recursively Download 
```
cd myfoldername
prompt OFF
recurse ON
mget *
```