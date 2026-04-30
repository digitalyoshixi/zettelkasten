---
tags:
  - security
---
A vulnerability in all Linux systems from 2017-2026 that use the [[authencesn]] service.
Lets unpriviledged user trigger a deterministic 4-byte write into any page cache of a readable system file.
Allows editing a [[setuid]] binary to obtain root.

https://xint.io/blog/copy-fail-linux-distributions