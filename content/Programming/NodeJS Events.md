---
tags:
  - web
  - javascript
  - node
---
The asynchronous events that allow multiple threads to communicate.
# Process Event
Events are most commonly created and sent through the [[NodeJS Process]] global.
```js
process.on('exit')
```
This `'exit'` in particular is saying that this event will fire before the process is about to exit.
```node
process.on('exit', function(){
	// <insert callback function here>
})
```
You can make a callback function to run after this event is fired.
![[NodeJS Events-20240917032727451.webp|585]]
### Triggering An Event
```node
const { EventEmitter } = require('events'); //loading a library
const eventEmitter = new EventEmitter() // instantiating the event emitter

// make event and callback function
eventEmitter.on('lunch', () => {
	console.log("yum");
})

eventEmitter.emit("lunch"); // fire this event;
```