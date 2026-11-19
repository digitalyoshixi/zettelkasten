---
tags:
  - networking
---
# Capture Port
```
tcpdump -i et0 port 21
```
# Dump `en0` to file
```
tcpdump -w output.cap -s 0 -i en0
```