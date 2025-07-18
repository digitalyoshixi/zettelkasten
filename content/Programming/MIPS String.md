---
tags:
  - assembly
---
A mips version of a [[C String]].
# Boilerplate
```mips
data:
	mystring: .asciiz "mystring"
	mystringwithnl: .asciiz "mystring\n"
```
These strings will be zero terminated.