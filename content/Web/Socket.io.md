---
tags:
  - web
aliases:
  - Socketio
---
# Installation
```
npm i socket.io socket.io-client
```
# Concepts
- [[Socket.io On()]]
- [[Socket.io Emit()]]
- [[Socket.io Broadcast.Emit()]]
- [[Socket.io to()]]
# Boilerplate
### Client
```js
import { io } from "socket.io-client"

const socket = io('http://127.0.0.1:3000')

// recieve an event (connect event)
socket.on('connect', () => {
    console.log(`You connected to the server with id ${socket.id}`);
})

// send an event
socket.emit('myevent', 10, 'Hi', {a : "a"});
```
### Server
```js
const io = require("socket.io")(3000, {
    cors :{
        origin : ["http://localhost:8080"],
    }
}) // run on port 3000

io.on('connection', socket => {
    // established new connection
    console.log(socket.id);
    // listen for event 'myevent'
    socket.on('myevent', (number, string, object) => {
        console.log(number, string, object) 
    })
})
```