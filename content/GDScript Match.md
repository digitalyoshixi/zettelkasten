---
tags:
  - programming
  - godot
aliases:
  - GDScript Switch Statement
---
```python
enum Alignment {ALLY, NEUTRAL, ENEMY}
@export var my_alignment: Alignment

func _ready():
	match myalignment:
		Alignment.ALLY:
			print("hello friend")
		Alignment.NEUTRAL:
			print("I come in peace")
		Alignment.ENEMY:
			print("Taste my wrath!")
		_:
			print("")
```