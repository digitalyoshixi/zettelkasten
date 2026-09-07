---
tags:
  - programming
  - godot
---
A [[Godot Node]] used for [[Shared Authority Model]] [[Photon Fusion]].
- Is a child node of another node, tracks properties of that other node
- Every change of that property is sent to its peers
- If this node is marked as an authority by another peer, update the property given from the peer
# Custom Tracked Properties
1. Click on FusionSharedReplicator node > Bottom Panel > Add Property To Sync
# Properties
- Snap Distance: Max distance physics interpolation should work on
# GDScript
```go
extends CharacterBody2D

@onready var sync : FusionSharedReplicator = $FusionSharedReplicator

func _process():
	if sync.has_authority():
		var dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
		position += dir * SPEED * delta
		
	
```