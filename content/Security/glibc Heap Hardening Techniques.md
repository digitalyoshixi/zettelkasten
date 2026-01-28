---
tags:
  - os
  - memory
---
glibc's basic heap hardening methods:
- `export MALLOC_CHECK_= 1`
- `export MALLOC_PERTURB_= 1`
- `export MALLOC_MMAP_THRESHOLD_= 1`