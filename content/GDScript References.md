---
tags:
  - programming
  - godot
---
# Onready Example
```python
extends Node
# onready ensures that all child nodes are created
@onready var weapon - $Player/Weapon

func _ready():
	print(weapon.get_path())
```
# Direct Reference Example
```python
func _ready():
	$Label.text = "Hello World"
```
![[GDScript References-20251023182624688.webp]]