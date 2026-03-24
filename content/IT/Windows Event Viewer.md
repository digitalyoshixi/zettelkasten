---
tags:
  - windows
aliases:
  - eventvwr.msc
---
Windows collects logs of every event that happens in its programs. The logs are collected and can be viewed in the event viewer.
![[Windows Event Viewer-20240706023925443.webp]]
# Logs
```
C:\Windows\System32\winevt\Logs
```
### Windows Logs
There are 4 categories within windows' logs:
1. **System:** Logs about drivers and system files
2. **Application:** Logs generated from applications that are not included in the System category
3. **Setup:** Records setup and update events
4. **Security:** Security events and failed authentication events. These are incredibly common
# Event Levels
- **Verbose:** Extra information that may be useful in troubleshooting
- **Information:** Something that suceeded
- **Warning:** Events that warn of future issues
- **Error:** Something went wrong
- **Critical:** Unexpected behaviors like sporadic system shutdowns
# Custom Views
These are log filters.
![[Windows Event Viewer-20240706024648654.webp]]
If you want to make your own, then right click custom view key > Create Custom View.
# Common Event Ids
- 4624: Logon events
- 4648: Admin logon
- 4656: Access attempt to object is made
- 4660: Object is deleted
- 4653: Attempt to open object (4656) is successful
# Tips
- [[Windows Enable Object Access Logging]]