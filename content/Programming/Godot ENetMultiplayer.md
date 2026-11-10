---
tags:
  - programming
  - godot
---
# Main.gd
```go
func _ready() -> void:
	if OS.has_feature('server'):
		Network.start_server()
		add_world()

func on_join():
	Network.join_server()
	add_world()

func add_world():
	var new_world = WORLD_FOREST.instantiate()
	get_tree().current_scene.add_child.call_deferred(new_world)
	
```
# MultiplayerHandler.gd
```go
var enet_peer := ENetMultiplayerPeer.new()
const PLAYERSCENE = preload("uid://....")

func _ready():
	add_to_group("Players")

var PORT = 9999
var IP_ADDRESS = '127.0.0.1'

func start_server():
	enet_peer.create_server(PORT)
	multiplayer.multiplayer_peer = enet_peer
	# connect signal when peer is connecting
	multiplayer.peer_connected.connect(add_player)

func join_server():
	enet_peer.create_client(IP_ADDRESS, PORT)
	multiplayer.peer_connected.connect(add_player)
	multiplayer.peer_disconnected.connect(remove_player)
	multiplayer.connected_to_server.connect(on_connected_to_server)
	multiplayer.multiplayer_peer = enet_peer
	
func on_connected_to_server():
	add_player(mutliplayer.get_unique_id())
	
func add_player(peer_id : int):
	if peer_id == 1:
		# skip self
		return
	# add player
	var new_player = PLAYERSCENE.instantiate()
	new_player.name = str(peer_id)
	get_tree().current_scene.add_child(new_player, true)
	
func remove_player():
	if peer_id == 1:
		leave_server()
	var players : Array[Node] = get_tree().get_nodes_in_group("Players")
	var player_to_remove = players.find_custom(func(item) : return time.name == str(peer_id))
	if player_to_remove != -1:
		players[player_to_remove].queue_free()

func leave_server():
	multiplayer.multiplayer_peer.close()
	multiplayer.multiplayer_peer = null
	clean_up_signals()

func clean_up_signals():
	multiplayer.peer_connected.disconnect(add_player)
	multiplayer.peer_disconnected.disconnect(remove_player)
	multiplayer.connected_to_server.disconnect(on_connected_to_server)
```