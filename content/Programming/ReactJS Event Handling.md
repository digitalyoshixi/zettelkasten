---
tags:
  - react
  - javascript
---
Events like:
- Clicks
- Mouse Movements
- Keyboard events
Can be detected with event handling methods.
```js
<button onClick={handleClick} />
<input onChange={handleChange} />
<form onSubmit={handleSubmit} />
```
# Event Handling Example
```js
function RedAlert(){
	const handleClick = () => {
		alert("BRRRRRRRRRRING")
	}
	return (
		<button onClick={handleClick}>
			Click ME!!
		</button>
	)
}


```