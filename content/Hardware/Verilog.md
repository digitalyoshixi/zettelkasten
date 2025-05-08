---
tags:
  - programming
---
A [[Hardware Description Language|HDL]] that is:
- Weakly typed
- Concise
- Deterministic
- [[C]]-like
# Installation/Setup
1. With [[VSCode]], install
   ![[Verilog-20250508023354797.webp]]
2. `yay -S iverilog`
3. `yay -S gtkwave`
# Simulating `.v` File
1. Write the `.v` file
2. `iverilog -o output.vpp input.v`
3. `vpp output.vpp`
4. `gtkwave output.vcd`