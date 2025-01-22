---
tags:
  - llvm
---
A top-down parser that is back-tracking. It also:
- Allows for mutually recursive functions where each function implements [[Non-terminals]]
# Process
Continue deriving from [[Productions]] until you match the required character in the input. If you get stuck, backtrack
# Example
https://www.youtube.com/watch?v=nv9J5Jb7IxM
![[Drawing 2025-01-01 17.19.20.excalidraw]]