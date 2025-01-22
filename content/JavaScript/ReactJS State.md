---
tags:
  - react
  - javascript
---
A state is a variable components can use.
To manage state, you need to use special [[ReactJS Hooks]] `useState()` and `useReducer()`.
# State & [[Document Object Model|VDOM]] connection
Everytime a setState() is called, the VDOM render is updated and the affected component is rerendered.
# Example useState()
![[ReactJS State-20240918031455684.webp]]
```js
function Likes(){
	const [likes, setLikes] = useState(0)
	const handleClick = () => {
		setLikes(likes + 1)	
	}


	return(
		<button onClick={handleClick}>
			Likes: {likes}
		</button>
	)

}
```
useState() can only be used in the main component function, helper functions must have these variables passed as arguments to use them
# setState() In the component function
```js
function Message(){
    const [count, setCount] = useState(1);
    setCount(2)
    return (
        <p>
            Hello {count}
        </p>
    );
}
```
Having setState() in the component function like this will cause an infinite loop because:
- Everytime a setState() is called, the VDOM reruns the component code
- When the component re-renders, it claled setState()
This will make the component render infinitely
### Countermeasures
You can make the setState() only called through an active function like:
```js
function Message(){
    const [count, setCount] = useState(1);
    return (
        <div>
        <p>Hello {count}</p>
        <button onClick={() => setCount(count + 1)}></button>
        </div>
    );
}
```
You could use [[ReactJS Effects]] with a empty array as a second argument to prevent multiple executions.
```js
function Message(){
    const [count, setCount] = useState(1);
    useEffect(() => {
        setCount(2)
    }, []);
    return (
        <p>Hello {count}</p>
    );
}
```