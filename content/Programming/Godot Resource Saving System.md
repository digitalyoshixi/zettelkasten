---
tags:
  - programming
  - godot
---
Two files
![[Godot Resource Saving System-20251227191209446.webp]]
# Save Resource
```python
class_name SaveResource
extends Resource

@export var coins: int
```
# Save Manager
```python
class_name SaveManager
extends Node

const SAVE_PATH = "user://savegame.tres" # text format for debugging

var current_save : SaveResource

var default_save_data : Dictionary = {
	"coins" : 0
}

func init_new_save() -> void:
	current_save = SaveResource.new()
	for key in default_save_data:
		current_save.set(key, default_save_data[key])

func save_game() -> void:
	if not current_save:
		printerr("no save data exusts")
		return
	var err = ResourceSaver.save(current_save, SAVE_PATH)
	if err != OK:
		printerr("failed to save: %s" % error_string(err))
	else:
		print("Game saved at: %s" % SAVE_PATH)

func load_game() -> bool:
	if not ResourceLoader.exists(SAVE_PATH):
		print("no save found, making enw save")
		init_new_save()
		return false
	
	var loaded_resource = ResourceLoader.load(SAVE_PATH, "", ResourceLoader.CACHE_MODE_IGNORE)
	if (loaded_resource is SaveResource):
		current_save = loaded_resource
		print("game loaded successfully")
		return true
	else:
		print("failed to load save, making a new one")
		init_new_save()
		return false
		
func get_save_data(key):
	return current_save.get(key)

func update_save_data(key, val) -> void:
	print("updated local save")
	current_save.set(key, val)
	print(key, " : ", get_save_data(key))

```