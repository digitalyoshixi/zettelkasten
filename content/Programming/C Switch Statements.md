---
tags:
  - c
  - cpp
---
Its quicker than [[C Conditional Statements]] exclusive for integral types like:
- Integer
- Double
- Char
You may see that you need `break;` statements at the end of every case. Well, they didn't make the switch statement so well. The C authors apoligize for it. but anyhow, this is [[Defensive Programming]]
# Example
```c
int c; 
scanf("%d",c);

switch (c){

	case 'a':
		break;
	case 'b':
		break;
	default:
		break;
}
```
