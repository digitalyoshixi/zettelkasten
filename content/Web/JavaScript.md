---
tags:
  - javascript
  - programming
---
A programming language used in [[Webapp|Webapps]] promoted for its:
- Adaptability
- Fast scalibility
# Concepts
### Theory
- [[JSON|Javascript Object]]
- [[Javascript Prototype]]
- [[Javascript Object Inheritance]]
### Fundamental
- [[Javascript Semicolon]]
- [[Javascript Variable]]
- [[Javascript For Loop]]
- [[JavaScript Console]]
- [[Javascript Datatypes]]
- [[Javascript Function]]
- [[Javascript Catch()]]
- [[Javascript Arrow Function]]
- [[Javascript Async]]
- [[Javascript Export]]
- [[Javascript Class]]
- [[Document Object Model|DOM]]
- [[Javascript Fetch]]
- [[Javascript Destructuring]]
- [[Javascript Local Storage]]
- [[Javascript Equivalences]]
- [[Javascript Base64]]
- [[Javascript map]]
- [[Javascript apply]]
- [[Javascript reduce]]
# Boilerplate
```js
const apiUrl = "https://jsonplaceholder.typicode.com/users/1"; 
let clickCount = 0; 

clickCount = clickCount + 1;

function formatGreeting(name) {
  return `Hello, ${name}! Welcome back.`; 
}

const calculateTotal = (price, taxRate) => {
  return price + (price * taxRate);
};

console.log(formatGreeting("Alex")); 
console.log(calculateTotal(100, 0.13)); 


const titleElement = document.getElementById("main-title");
const buttonElement = document.getElementById("action-btn");

let clicks = 0;

buttonElement.addEventListener("click", () => {
  clicks++;
  titleElement.textContent = `You clicked the button ${clicks} times!`;
  titleElement.style.color = "royalblue";
});
```

