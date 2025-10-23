---
tags:
  - programming
  - godot
---
These are specific events that come from:
- Key press
# Example Space Press
1. `Project` > `Project Settings` > `Input Map` > `Add New Action` > `Add` > `+` > Select your action
2. Write a input handler function in [[GDScript]]
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