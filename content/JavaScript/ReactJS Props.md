---
tags:
  - react
  - javascript
---
Used to pass data to [[ReactJS Component|Components]].
1. Make a prop 
```js
<Greeting text={'yo'}/>
```
2. Use prop value
```js
function Greeting(props){
	return <h1>{props.text}</h1>
}
```

# Passing As Object
In app.js:
```jsx
const myobject = {
	a : 20,
	b : 40
}
function App(){
	return (
		<Mycomponent a={myobject.a} b={myobject.b}/>
	)
}
```
# Concepts
- [[ReactJS Children]]
- [[ReactJS Keys]]