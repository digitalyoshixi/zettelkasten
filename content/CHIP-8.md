---
tags:
  - programming
  - cpu
  - esolang
aliases:
  - CHIP 8
---
An [[Interpreter|Interpreted]] programming language.
# Concepts
- [[CHIP-8 ROM]]
- [[CHIP-8 Font]]
- [[CHIP-8 Display]]
- [[CHIP-8 Stack]]
# Specifications
- Memory: 4KB (4096 bytes) of [[Random Access Memory|RAM]]
- Display: 64 x 32 pixels, monochrome (black and white)
- A [[Program Counter Register|PC]] register
- A [[Index Register]] `I`
- A [[OS Stack|Stack]] for 16-bit addresses
- A 8-bit delay timer decremented at rate of 60 Hz until it reaches 0
- A 8-bit sound timer that functions as delay timer, but which also gives a beeping sound so long as its not 0
- 16 16-bit general purpose variable registers:
	- `V0`
	- `V1`
	- ...
	- `VF` - also used as [[Carry Bit|Carry Flag]] register
- Font characters represented as [[Bitmap]] 4px by 5px tall