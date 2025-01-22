---
tags:
  - javascript
  - react
---
If you want to return multiple [[ReactJS Component|Components]], you can put them in a fragment.
```js
return {
	<>
		<Header />
		<Main />
	</>
}
```
This is just returning an empty component.