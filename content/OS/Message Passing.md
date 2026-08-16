---
tags:
  - os
  - networking
---

Very useful method of data sharing most commonly used in a network. To use this system you create a communication link. These links can be direct, indirect, synchronous, asynchronous, automatic or explicit. Processes must send messages and receive messages. These messages can have a fixed or variable size.

  

### Message passing(Naming)

This concerns direct or indirect communication links. This is how the 2 processes identify each other

Direct communication:

send(P,message), receive(Q,message) -- sender and receiver both know each other(symmetric)

Or:

send(P,message), receive(message) -- does not need to know the recipient(asymmetric)

If either the sender or receiver change names, then the link is broken

  

Indirect communication:

Messages are sent and received from ports. Processes communicate if they have a shared port

send(A,message), receive(A,message)

This port system allows for more than one process to communicate. We set restrictions on how messages are received. For example, we dont want 2 processes to receive the same message, so we limit how many processes can read this message. Round robin is an algorithm to determine where a message can be sent.

  

### Message passing(Synchronization)

Block = asynchronous

Non-Block = synchronous

  

A blocking/async send is a send that waits for the last message to be received, only then it will send.

A non-blocking/sync send is a send that sends and does not wait for it to be received.

blocking receive is a receive that stalls the program until it receives a message.

Non-blocking receive, receives either a message or null value.