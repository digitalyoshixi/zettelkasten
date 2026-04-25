---
tags:
  - godot
  - game_dev
---
A [[Dynamically Typed]] [[Python]]-based language.
- [[Zero Indexed]]
# Concepts
### Fundamental
- [[GDScript Variables]]
- [[GDScript Comment]]
- [[GDScript Constants]]
- [[GDScript Data Types]]
- [[GDScript String]]
- [[GDScript Enum]]
- [[GDScript Typecasting]]
- [[GDScript Functions]]
- [[GDScript Conditional Statement]]
- [[GDScript For Loop]]
- [[GDScript While Loop]]
- [[GDScript Match]]
### Specific
- [[GDScript Vector]]
- [[GDScript Random Number]]
- [[GDScript References]]
- [[Godot Actions]]
- [[Godot Signals]]
- [[Godot Getters and Setters]]
- [[GDScript Class]]
- [[GDScript Lambda Function]]
# Boilerplate
```python
extends Node

func _ready():
	print("Hello World")
	
func _input(event):
	if event.is_action_pressed("my action name"):
		print("pressed")
	if event.is_action_released("my action name"):
		print("released")
		
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
```