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
- [[CHIP-8 Timer]]
- [[16 Key Keypad]]
- [[Fetch Decode Execute]]
- [[CHIP-8 Registers]]
- [[CHIP-8 Instructions]]
- [[CHIP-8 Test Suite]]
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
	- `I` - instruction register
- Font characters represented as [[Bitmap]] 4px by 5px tall
- Speed of ~ 700 instructions per second is natural
# References
- https://tobiasvl.github.io/blog/write-a-chip-8-emulator/