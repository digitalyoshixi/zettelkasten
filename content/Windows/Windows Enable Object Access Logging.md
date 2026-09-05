---
tags:
  - windows
  - forensics
---
Setting up file/folder access logs for [[Windows Event Viewer]].
```
auditpol /set /category:"Object Access" /success:enable /failure:enable
```