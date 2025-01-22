---
tags:
  - math
---
**Not as good as the IROC prime method because values are relative to a point**
Requires: 
- Formula
- 2 Points
A method for finding the [[Instantaneous Rate of Change|IROC]]
How this is done is by creating a formula for AROC for every offset of x.
it goes like this:
f(x$_2$) - f(x) / x$_2$ - x
Find algebraically, the new function that results from this. and find the constant value. that is your instantaneous velocity.

## Example
For example, function `f(x) = -0.5x^3+2x+3`and we have a point `(2,3)`
![[Pasted image 20230914181035.png]]
to find the instant velocity, we need to find 2 formulas.
f(2) and f(2+o)
```
f(2) = -0.5(2)^3+2(2)+3
	 = 3
```
```
f(2+o) = -0.5(2+o)^3+2(2+o)+3
	   = -0.5(o^3+6o^2+12o+8) + 4 + 2o + 3
	   = -0.5o^3 -3o^2 -4o + 7
```
so then its `f(2+o) - f(2) / o`
```

```

