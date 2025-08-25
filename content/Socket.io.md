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
# Boilerplate
### Client
```js
import { io } from "socket.io-client"

const socket = io('http://127.0.0.1:3000')
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
})
```