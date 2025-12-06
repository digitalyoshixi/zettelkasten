---
tags:
  - programming
---
Instructions are divided by [[Binary|Nibble]].
# Structure
- First [[Binary|Nibble]]: Instruction type
- Second [[Binary|Nibble]] (`X`):  one of the registers `V0`-`VF`
- Third [[Binary|Nibble]] (`Y`): one of the registers `V0`-`VF`
- Fourth [[Binary|Nibble]] (`N`): A 4-bit number
- Fourth + Fifth [[Binary|Nibble]] (`NN`): A 8-bit immediate number
- Fourth + Fifth + Sixth [[Binary|Nibble]] (`NNN`): A 12-bit memory address
# Instructions Table
| Code   | Description                         |
| ------ | ----------------------------------- |
| `00E0` | Clear screen                        |
| `1NNN` | Jump                                |
| `6XNN` | Set register `VX`                   |
| `7XNN` | Add value to register `VX`          |
| `ANNN` | Set memory register `I`             |
| `DXYN` | Display/Draw                        |
| `0NNN` | Execute subroutine at address `NNN` |
