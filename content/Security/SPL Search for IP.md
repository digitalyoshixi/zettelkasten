---
tags:
  - security
---
```
index=_internal sourcetype=netflow | search ip_dst=~”\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}”
```
