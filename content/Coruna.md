---
tags:
  - malware
  - security
---
A [[iOS]] [[Spyware]].
# Browser Sandbox Escape
- Minified javascript
- JSON.parse() of arrays
- Uses base64 encoded functions
- [[Just-in-time Compilation|JIT Optimizes]] a function by calling it one million times
	- Confuses JIT compiler to allow the function to perform out of bounds write
- Uses out-of-bound primative to chain read and write primatives