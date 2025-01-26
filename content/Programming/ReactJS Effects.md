---
tags:
  - react
  - javascript
aliases:
  - Side Effects
  - useEffect()
---
For requesting browser [[Application Program Interface|API]] or sending/recv to server
Best done in a event handler 
![[ReactJS Effects-20240918033211537.webp]]
If it can't be done in an event handler, then use `useEffect()`
# `useEffect( () => {}, [])`
An example is commonly this is used in fetching user data after page load
![[ReactJS Effects-20240918033315760.webp]]
The first parameter is the callback function
The second parameter is what to watch for changes
# First Run Callback
Whenever you render the component for the first time, the useEffect callback function will be ran automatically.
After the first render, it will run 