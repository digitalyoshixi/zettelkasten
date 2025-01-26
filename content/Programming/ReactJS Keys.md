---
tags:
  - react
  - javascript
---
Used to tell components apart.
Often used along with [[ReactJS List]] and provide a similar use as index
```js
{items.map(item => (
	<Component key={item.id}/>
))}
```
A key is a unique string/number