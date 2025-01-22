---
tags:
  - reverse_engineering
aliases: []
---
how programs are explored and managed with angr
```python
import angr, monkeyhex
proj = angr.Project('binarypath')
```
# Attributes
### proj.arch
Returns the [[CPU Architecture]] and the [[Endness]] of the file
![[angr Project-20240714162208451.webp]]
### proj.entry
Returns the address of the entry point of the program in the corresponding [[Endness]] format
### proj.filename
Returns a string of the filepath.
### proj.loader
returns the [[angr Loaded Object|angr Loaded BInary]] of the file
![[angr Project-20240714170658703.webp]]
### proj.factory
Creates a [[angr Factory]] object
### proj.analyses.*
A whole bunch of [[angr Analysis Tools]] 