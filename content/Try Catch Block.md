---
tags:
  - programming
aliases:
  - Try Block
  - Exception Handling Block
---
A block comprised of:
```java
try{
	; body
}
catch (exception){

}
```
# Implemenation
- Try statement takes a snapshot of [[Stack]]
- Throw re-instantiates that snapshot of the stack 
- If the return value is an exception, it executes the catch statement