---
tags:
  - web
---
A background task to perform: 
- Caching
- Background sync
- Listens to push notifications
# Registering A Worker
```js
<script>
	if ('serviceWorker' in navigator){
		navigator.serviceWorker.register('/sw.js');
	}
</script>
```