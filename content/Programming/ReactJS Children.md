---
tags:
  - react
  - javascript
---
These are [[ReactJS Props]] that are [[ReactJS Component]]
As long as the [[ReactJS Component]] has [[JSX]] that has open and close tags, a child can be given to them.
![[ReactJS Children-20240918013148950.webp|388]]
The children props are commonly used when you want elements that share the same layout as the parent
# Accessing
```js
function Greet(props){
	console.log(props.children)
}
```