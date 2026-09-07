---
tags:
  - programming
---
A [[Godot Node]] used for spawning scenes for all clients.
# GDScript
```go
@onready spawner : FusionSpawner = $FusionSpawner
const PlayerScene = preload("res://scenes/player.tscn")

func _ready():
	spawner.add_spawnable_scene(PlayerScene)
	var player = spawner.spawn()
```
