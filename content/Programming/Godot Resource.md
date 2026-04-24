---
tags:
  - programming
  - godot
---
[[Godot Nodes]] that can be saved to disc. Stores data and code.
Requires a [[GDScript]] definition and `.tres` containers.
# Example
### `entity_resource.gd`
```python
class_name CollectableResource
extends Resource

@export var id : Constants.EntityID # TODO: convert to ENUM instead
@export var exp_gain : int
@export var energy_gain : int
@export var hierarchy : Array[Constants.FoodHierarchy]

func _init(id = "", exp_gain = 0, hp_gain = 0, energy_gain = 0, hierarchy=[]):
	self.id = id
	self.exp_gain = exp_gain
	self.energy_gain = energy_gain
	self.hierarchy = hierarchy
```
### `egg_resource.tres`
Make this link to `entity_resource.gd` and change the data