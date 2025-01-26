---
tags:
  - react
  - javascript
aliases:
  - Components
---
These are the UI elements of your website.
A component can be: 
- Button
- Input
- Entire page (root component)
Every JavaScript component is a function that returns [[JSX]] 
# Example Component (Button)
```js
function MyButton() {
	return {
		<button> I am a button </button>	
		// returns button is JSX you can also make it with createElement('button', null, "HI")
		
	}; 
}
export default MyButton()
```
# Component Types
### Functional Component
Returns [[JSX]] that describes the UI. Most common way to write components now
Used to be the only component that can't use states, now all classes components can use states with [[ReactJS Hooks]]
![[ReactJS Component-20240920005510039.webp]]
### Class Component
Class extending another component class.
Used to be the only component that can use states, now all classes components can use states with [[ReactJS Hooks]]
![[ReactJS Component-20240920005517313.webp]]

# Concepts
- [[ReactJS Component Data]]