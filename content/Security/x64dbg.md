---
tags:
  - reverse_engineering
  - reverse_engineering
  - debugging
---
# Techniques
- [[x64dbg Default Breakpoints]]
- [[x64dbg Strings References]]
- [[x64dbg Find PE Header]]
- [[x64dbg Intermodular Calls]]
- [[x64dbg Extract DLL]]
# Buttons & What they do
| button name | icon | purpose |
| ---- | ---- | ---- |
| restart | ![[x64dbg-20231228214956698.webp]] | rerun the code from first breakpoint |
| close | ![[x64dbg-20231228215003800.webp]] | close current program |
| run | ![[x64dbg-20231228215224448.webp]] | run until next breakpoint |
| pause | ![[x64dbg-20231228215239973.webp]] | Pause program execution. *this means the loops/IO end briefly* |
| step into | ![[x64dbg-20231228215246026.webp]] | step forwards 1 step, can go into functions |
| step over | ![[x64dbg-20231228215252178.webp]] | step forwards 1 step, will pass over funtions |
| trace into | ![[x64dbg-20231228215256983.webp]] |  |
| trace over | ![[x64dbg-20231228215301638.webp]] |  |
| execute til return | ![[x64dbg-20231228215309296.webp]] | run until we hit a 'ret'. useful if you want to get out of a function |
| run to user code | ![[x64dbg-20231228215314476.webp]] |  |

# C Functions & What they do
- [[printf Debugging]]
- [[]]

# Hotkeys
**CTRL+G**: Go to a memory address