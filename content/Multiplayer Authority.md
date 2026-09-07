---
tags:
  - game_dev
---
A concept in multiplayer games where certain scenes of a game have their properties controlled by one client:
- Client's own player model
- Client's own items
Client will send these statuses to peers or server and will be trusted.
# Godot Implementation
```go
extends Node

func _enter_tree() -> void:
	set_multiplayer_authority(1) # trust all of client 1's  client
```