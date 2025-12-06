---
tags:
  - programming
  - cpu
  - esolang
---
A [[ROM Image]] for [[CHIP-8]] architecture.
- 4096 bytes max size
- First 512 bytes should be used for assets. (`000` - `1FF`)
	- [[CHIP-8 Font]]
- Byte `1FF`-`FFF` contains program data