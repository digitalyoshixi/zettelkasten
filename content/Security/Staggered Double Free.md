---
tags:
  - security
  - os
---
A [[Double Free]] technique that evades detection.
1. Allocate memory for `a`
2. Free `a`, note that you still have a reference to `a`
3. Allocate memory for `b` - it will take the chunk of a
4. Free `b`
5. Free `a`