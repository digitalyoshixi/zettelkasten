---
tags:
  - web
---
A background task to perform: 
- Caching
- Background sync
- Listens to push notifications
# Process
1. First visit - service worker is installed (Client -> Server)
2. Online mode - service worker acting as a proxy (Client -> Service Worker -> Server)
3. Offline mode - service worker responding with cached responses (Client -> Service Worker -> Cache)
# Registering A Worker
```js
<script>
	if ('serviceWorker' in navigator){
		navigator.serviceWorker.register('/sw.js');
	}
</script>
```