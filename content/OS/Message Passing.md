---
tags:
  - os
  - networking
aliases:
  - Communication Link
---
A method to setup [[Interprocess Communication|IPC]] for networked processes or in [[Microkernel]] systems.
- To use this system, you must create a communication link
- Messages can be fixed or variable size
# Link Types
### Direct vs Indirect
- Direct: Sender and reciever send directly to each other
	- `send(P,message)`
	- `recieve(Q,message)` or `receive(message)` (does not need to know the recipient)
- Indirect: Sender and reciever have a shared port they read/write to. Allows more than two parties to communicate too.
	- `send(A,message)`
	- `receive(A,message)`
### Synchronous vs Asynchronous
- Asynchronous (block)
	- Send waits for last message to be recieved before sending
	- Recieve stalls program until a message is recieved
- Synchronous (non-block)
	- Send does not wait for recieve
	- Recieve either a message or null value
### Reliable vs Best Effort
- Reliable:
	- Messages guaranteed to be delivered, on failure, sender is notified
- Best-Effort:
	- Messages may or may not be delivered, could be corrupted or come after a delay
