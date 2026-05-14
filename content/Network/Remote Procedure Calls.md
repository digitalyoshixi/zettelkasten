---
tags:
  - networking
aliases:
  - RPC
---
An abstraction of network details that allows the caller to call a function in a program running on another device.
Requires a distributed system like [[Peer to Peer|P2P]].
- Program can request services without knowing network details
Contrasted to [[Interprocess Communication|IPC]] that is communication in the same device.
# Process
1. Server exposes a RPC service
2. Client sends [[Serialization|Marshalled]] object to RPC endpoint
3. Reciever deserializes and performs function, returns result in serialized form
# Concept
- [[protobuff]]