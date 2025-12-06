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
| Code   | Description                                                                                                            |
| ------ | ---------------------------------------------------------------------------------------------------------------------- |
| `00E0` | Clear screen                                                                                                           |
| `1NNN` | Jump, or set [[Program Counter Register\|PC]] to `NNN`                                                                 |
| `6XNN` | Set register `VX`                                                                                                      |
| `7XNN` | Add value to register `VX`. [[Overflow Flag]] not affected                                                             |
| `ANNN` | Set memory register `I` to `NNN`                                                                                       |
| `DXYN` | Display/Draw                                                                                                           |
| `0NNN` | Execute subroutine at address `NNN`                                                                                    |
| `00EE` | Return from subroutine by popping last address from stack                                                              |
| `2NNN` | Call subroutine at memory location `NNN`                                                                               |
| `3XNN` | Branch statement if `VX` = `NN`                                                                                        |
| `4XNN` | Branch statement if `VX` != `NN`                                                                                       |
| `5XY0` | Branch statement if `VX` = `VY`                                                                                        |
| `9XY0` | Branch statement if `VX` != `VY`                                                                                       |
| `8XY0` | Set the value `VX` to `VY`                                                                                             |
| `8XY1` | Set `VX` to [[Bitwise OR]] of `VX`, `VY`                                                                               |
| `8XY2` | Set `VX` to [[Bitwise AND]] of `VX`, `VY`                                                                              |
| `8XY3` | Set `VX` to [[Bitwise XOR]] of `VX`, `VY`                                                                              |
| `8XY4` | Set `VX` to addition of `VX`, `VY`. Affects [[Carry Bit\|Carry Flag]]                                                  |
| `8XY5` | Set `VX` to subtraction `VX` - `VY`. <br>Set `VF` to 1 if we have a natural remainder<br>Set `VF` to 0 if we underflow |
| `8XY7` | Set `VX` to subtraction `VY` - `VX`<br>Set `VF` to 1 if we have a natural remainder<br>Set `VF` to 0 if we underflow   |
| `8XY6` | Put value of `VY` into `VX`, then [[Bitwise Right Shift]] by one<br>Set `VF` to the bit that was shifted out.          |
| `8XYE` | Put value of `VY` into `VX`, then [[Bitwise Left Shift]] by one<br>Set `VF` to the bit that was shifted out.           |
| `BNNN` | Jump with offset `NNN` + `V0` used as [[Jump tab]]                                                                     |
