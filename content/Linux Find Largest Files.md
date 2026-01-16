---
tags:
  - linux
---
For finding the largest file in the current directory:
```
du -sh * | sort -rh | head -n 10
```