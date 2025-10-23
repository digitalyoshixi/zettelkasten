---
tags:
  - godot
  - game_dev
---
A [[Dynamically Typed]] [[Python]]-based language.
[[Zero Indexed]]
# Concepts
- [[GDScript Variables]]
- [[GDScript Comment]]
- [[GDScript Constants]]
- [[GDScript Data Types]]
- [[GDScript Typecasting]]
- [[GDScript Vector]]
- [[GDScript Functions]]
- [[GDScript Conditional Statement]]
- [[GDScript References]]
- [[Godot Actions]]
- [[GDScript Random Number]]
- [[GDScript For Loop]]
- [[GDScript While Loop]]
- [[GDScript String]]
- [[GDScript Dictionary]]
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
```