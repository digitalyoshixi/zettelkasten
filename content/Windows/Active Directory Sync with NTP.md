---
tags:
  - windows
  - active_directory
---
```
w32tm /config /manualpeerlist:time.windows.com,0x8 /syncfromflags:MANUAL
net stop w32time
net start w32time
w32tm /config /update
w32tm /resync /rediscover
```
