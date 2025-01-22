---
tags:
  - web
---
Webapps where there is only a single `index.html` that changes on the fly.
![[Single Page App Model-20240802023342105.webp]]
Client requests information, web page instantly returns the webpage either:
- Webpage saved in cache
- A empty webpage
	- A JS file is given from the [[Content Delivery Network|CDN]]
	- the JS file sends an API to your server
	- server returns the entire webpage