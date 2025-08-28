---
tags:
  - networking
  - web
---
A function that will send a message to all sockets listening except for the current sending socket.
```js
socket.broadcast.emit('myeventresponse', number);
```