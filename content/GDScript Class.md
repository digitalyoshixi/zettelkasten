---
tags:
  - programming
  - godot
---
`character.gd`
```python
class_name Character
extends Node

@export var profession : String
@export var health : int

func die():
	health = 0
	print(profession + " died")
```
`main.gd`
```python
extends Node

func _ready():
	var myCharacter : Character = Character.new()
```