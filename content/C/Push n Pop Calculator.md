---
tags:
  - c
  - math
---
A calculator can be implemented easily with only using a stack and some minor CPU calculations.

The calculations must all be done in reverse polish notation.
So, a calculation like:
`(2+5) * (1+3)`
turns into
`2 5 + 1 3 + *`

Now the program pseudocode looks like this:
```c
while (there is still an operation/operand){
	if (operand){
		push operand;
	}
	else if (operation){
		pop last 2 oerands;
		do operation;
		push result;
	}
	else {
		error;
	}
}
```
