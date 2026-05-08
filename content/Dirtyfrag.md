---
tags:
  - security
  - linux
aliases:
  - Dirty Frag
---
A [[Linux]] [[Privilege Escalation]] attack.
Builds upon [[Copy Fail]] to trigger a out-of-bound write  through network sockets via [[xfrm-ESP]] Page-Cache WRite.
Involves the manipulation of pipe page cache fails:
- `PIPE_BUF_FLAG_CAN_MERGE`
- [[splice()]]
Can overwrite read-only file data in page cache.