---
tags:
  - debugging
---
This is a [[Go|Golang]] debugger
# Installation
```
yay -S delve
```
# Debugging Compiled Binary
```
dlv exec ./binary
```
# Debugging Compile&Debug Binary
```
dlv debug ./binary
```
# Debugging Binary that uses STDIN
https://github.com/go-delve/delve/issues/1274
1. `dlv --headless exec ./chal`. You will be given a port
2. `dlv connect :XYZ`, this is your debugger. The other instance is now your stdin