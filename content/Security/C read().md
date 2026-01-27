---
tags:
  - c
---
A function that reads from stdin
`read(0, var1, size)`
# Bin Exploitation
1. End your user input early with a null terminator and then hide your payload after the null terminator
2. Do not include a null terminator in your input and let the program read infinitely