---
tags:
  - programming
  - game_dev
  - networking
---
One-time [[Remote Procedure Calls|RPC]] events to call a function.
```go
@rpc("any_peer", "call_local")
func show_message(text: String):
    $MessageLabel.text = text

func send_message():
    Fusion.rpc(show_message, "Hello!")
```