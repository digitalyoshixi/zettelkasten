---
tags:
  - programming
  - verification
---
# Example
```lean
structure Point where
	x : Float
	y : Float

def zeroX (p : Point) : Point :=
{p with x := 0}

#eval (zeroX {x : 4.3, y := 3.4} )
// {x := 0.0000, y := 3.400}
```
- Replaces the x in the struct with 0