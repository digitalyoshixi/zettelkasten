---
tags:
  - web
  - networking
---
A function that will send a message to all sockets listening.
[[Socket.io Broadcast.Emit()]] will prevent the current socket from recieving this message.
# Boilerplate
```js
socket.emit('myevent', 10); // send the value 10 as an argument, for the event 'myevent'
```