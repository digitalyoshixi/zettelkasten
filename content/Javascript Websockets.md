---
tags:
  - programming
  - javascript
---

```js
var websocket = newWebSocket();

function newWebSocket() {

	return new Promise(res => {
		let ws = new WebSocket("ws://www.mysite.com/chat");
	
		ws.onopen = function (evt) {
			newWebSocket.send("HI IM HERE");
			res(ws);
		}
		
		ws.onmessage = function (evt) {
			console.log(evt.data)
		}
		
		ws.onclose = function (evt) {
			console.log("disconnected")
		}
		
		
	})
}


```