---
tags:
  - c
---
Only one static variable may exist for a files. This is a lifesaver if the compiler complains about name collisions.

![[Static Name Collision Avoidance-20240131220317474.webp]]
2 files that share the same name, this will break.

But making these 2 variables static, then it will compile well and all is fine.
![[Static Name Collision Avoidance-20240131220349744.webp]]