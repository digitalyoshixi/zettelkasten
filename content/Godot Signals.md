---
tags:
  - programming
---
# Viewing Signals
Node -> `Signals`
![[Godot Signals-20251023184933234.webp|375]]
# Inheriting Signals
### Method 1: Connect
Double click signal from menu > Choose script to connect to
Then, you should get a green connection icon
![[Godot Signals-20251023185044497.webp|337]]
### Method 2: Programmatic Signals
Creation script:
```python
extends Node

signal leveled_up
signal mymessage(message : str)

func _ready():
	leveled_up.emit()
	mymessage.emit("congrats")
```
Hook script:
```python
extends Node

signal leveled_up
signal mymessage

func _ready():
	leveled_up.connect(_on_leveled_up)
	mymessage.connect(_on_mymessage)

func _on_leveled_up():
	print("YAY")
	pass
	
func _on_mymessage(msg): 
	print(msg)
```