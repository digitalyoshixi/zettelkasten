---
tags:
  - programming
  - godot
---
```python

@onready var nav_agent = $NavigationAgent2D
@export var target : Node2D

func _ready():
	call_deferred("seeker_setup")
	

func seeker_setup():
	await get_tree().physics_frame
	if target:
		nav_agent.target_position = target.global_position

func _physics_process(_delta):
	if target:
		nav_agent.target_position = target.global_position
	if (nav_agent.is_navigation_finished()):
		return
	var next_path_pos = nav_agent.get_next_path_position()
	self.velocity = self.global_position.direction_to(next_path_pos)
	
	move_and_slide()
```