---
tags:
  - devops
---
To rate of per $x$ seconds of query generation:
```
rate(prometheus_tsdb_head_chunks_created_total[1m])
```
Where it checks the number of chunks generated per second.
![[PromQL rate-20251030031213120.webp]]