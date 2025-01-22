---
tags:
  - javascript
  - web
aliases: []
---
Used as the [[NextJS Dynamic Route]]
These are files called `[param].js` to allow for dynamic pages.
![[NextJS Dynamic Routers-20241128011403480.webp]]
If you want to use this id, then you can do this:
```js
import {useRouter} from 'next/router'

export default function Car(){
	const router = useRouter()
	const { id } = router.query

	return <h1>Hello {id}</h1>
}
```
