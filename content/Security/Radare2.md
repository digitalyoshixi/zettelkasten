---
tags:
  - reverse_engineering
---
This is the ultimate package of reverse engineering tools. It can:
- Be a [[Disassembler]]
- Be a [[Debugger]]
- Be a [[Emulator]]
- Perform [[strings]] searches
- Parse [[Executable and Linkable Format|ELF]] and [[Portable Executable|PE]] headers
- Run [[Python]] scripts within it
It is not a stable product unlike [[Ghidra]], [[IDA]] or [[Binary Ninja]].
The GUI front-end is [[Cutter]]
# Install
`sudo pacman -S radare2`
# Quickstart
`radare2 -AA ./file`
Then run `i?` for help
`q` to exit out of menus
`CTRL+C` to exit out of prompts
### Analyze
- `aaa`
### Recon
- `izz ~..` view strings piped into less
- `afl` - view all functions
### Debugger
- `db main` - put break at main
- `db` - view all breakpoints
- `s main` step to main function
- `e stack.size = 128` - changing # bytes stack shows
- `F7` - step into
- `F8` - step out
### Views
- `v` - disassembler view
- `V` - hex editor view
- `V` > `p` > `p` - debugger view with stack
