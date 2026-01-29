---
tags:
  - os
  - memory
---
All the available memory left retrieved from the [[Operating System|OS]] to serve all potential malloc calls for a particular thread.
![[Memory Arena-20260129055011318.webp|372]]
# Number of Arenas
A concurrent application can support 
```c
limit = (32bit) ? number of codes * 2 : number of cores * 8
```