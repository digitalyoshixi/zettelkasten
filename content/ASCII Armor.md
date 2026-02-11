---
tags:
  - security
  - cryptography
---
A wrapping security tooling over [[Pretty Good Privacy|PGP]].
Consists of:
- Armor header line
- Armor headers that contain additional data
- [[Base64]] encoded [[Pretty Good Privacy|PGP]] data
- Optional [[Checksum]] for this data
- Armor tail line or footer
https://openpgp.dev/book/armor.html