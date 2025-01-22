---
tags:
  - react
  - javascript
---
Using [[ReactJS State]] for components.
![[ReactJS Controlled Components-20240918031806790.webp]]
# Example
![[ReactJS Controlled Components-20240918032047669.webp]]
```js
function ControlledInput(){
	const [value, setValue] = useState('')

	return(
		<input
			value={value}
			onChange={(e) => setValue(e.target.value)}	
		/>
	)
}
```