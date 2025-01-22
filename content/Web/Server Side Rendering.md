---
tags:
  - web
---
# Full SSR
![[Server Side Rendering-20240802025741429.webp]]
1. A Static HTML page is given. Buttons and forms wont work because there is no JS yet.
2. the JS is loaded by the CDN. This is slow on first load, but faster due to caching on subsequent loads
This is better than [[Single Page App Model]], because it avoids many intermediate stages. You just wait very long for the static HTML to load.
It also allows you to load other HTML elements while it is fetching the JS for content of another element.
![[Server Side Rendering-20240802030224911.webp]]
# Implementation

```js
export async function getServerSideProps({ params }){
	const req = await fetch(`http://localhost:3000/${params.id}.json`);
	const data = await req.json();
	return {
		props : { car : data},
	}
}
```
