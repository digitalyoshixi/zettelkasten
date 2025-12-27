---
tags:
  - programming
  - godot
---
# Loading/Saving
```python
class_name GameState extends Node

static var coins = 0

var config = ConfigFile.new()

func load_config() -> void:
	var err = config.load("user://save.cfg")
	if err != OK:
		return
	coins = config.get_value("Player", "coins")
	
func save_config() -> void:
	config.set_value("Player", "coins", coins)
	config.save("user://save.cfg")
	
```