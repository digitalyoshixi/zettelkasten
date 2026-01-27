---
tags:
  - security
aliases:
  - ROPGadget
---
A snippet of assembly code that ends in a `ret`
```
...
ret
```
# Rop Gadget Finder
```
pip install ROPgadget
```
### Usage
```
ROPgadget --binary ./myfile | grep -P "(mov|add|sub|pop) rdx"
```
