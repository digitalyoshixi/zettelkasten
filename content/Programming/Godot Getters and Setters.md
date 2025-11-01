---
tags:
  - programming
---
```python
extends Node

var chance := 0.2
var change_pct : int:
	get:
		return chance * 100
	set(value):
		chance = float(value) / 100.0

func _ready():
	print(change_pct) # will print 20
	change_pct = 40 # will change to 0.4
```