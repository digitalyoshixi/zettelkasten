---
tags:
  - programming
  - godot
---
# Structure
![[Godot Area2D-20251227191834195.webp]]
# Script
```python
extends Node2D

func _on_area_2d_body_entered(body):
	if body is Player:
		pass
```