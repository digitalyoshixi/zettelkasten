---
tags:
  - programming
  - javascript
---
Executes a [[Reducer Function]] for an array element to convert that array into a single value.
```javascript
const items = [
  { name: 'Apple', price: 1 },
  { name: 'Orange', price: 2 },
  { name: 'Mango', price: 3 },
];

const totalPrice = items.reduce((accumulator ,item) => {
  return accumulator += item.price;
}, 0)
```
- First argument is the [[Reducer Function]]
- Second argument is first argument to reducer function
- Third argument is second element to reducer function
- ...
- The list is sent as the last argument to the reducer function