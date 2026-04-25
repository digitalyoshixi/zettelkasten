---
tags:
  - programming
  - godot
---
# State.gd
```python
@abstract class_name State
extends Node

enum Name { IDLE, GROW, END }

var actor: Actor
var state_name: Name

func enter() -> void:
	# logic on enter
	pass

func exit() -> void:
	# logic on exit
	pass

@abstract func setup(actor : Actor -> void
@abstract func process_physics_frame(delta: float) -> Name

```
# states/IdleState.gd
```python
extends State
class_name IdleState

func enter() -> void:
	# logic
	pass
func exit() -> void:
	# logic
	pass
func setup(actor : Actor) -> void:
	# logic
	pass
func process_physics_frame(delta : float) -> State.Name:
	# logic
```
# StateMachine.gd
```python
extends Node

class_name StateMachine

@export var actor : Actor
@export var starting_state : State
@export var state_dictionary : Dictionary[State.Name, State]

var current_state : State

func setup() -> void:
	for key: State.Name in state_dictionary:
		state_dictionary[key].setup(self.actor)
	change_state(starting_state)

func change_state(new_state: State) -> void:
	if current_state:
		current_state.exit()
	current_state = new_state
	current_state.enter()

func process_physics_frame(delta: float) -> void:
	var new_state: State = state_dictionary[current_state.process_physics_frame(delta)]
	if new_state != current_state:
		change_state(new_state)
	actor.move_and_slide()
```