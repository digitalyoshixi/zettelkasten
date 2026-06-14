---
tags:
  - verification
  - programming
aliases:
  - Lean Structure
cssclasses:
---
A collection of types in one package.
# Example
```lean
structure Point where
	x : Float
	y : Float

def origin : Point := { x := 0.0, y := 0.0 }
#eval origin.x
#eval origin.y
```
# Constructor
A function of a [[Lean Struct]] used to create this structure.
- Default constructor attribute is `.mk`
### Constructor Overriding
If you dont want `.mk` as the constructor reference:
```lean
structure Point where
	point ::
	x : Float
	y : Float
```
- Then, `Point.point` is the constructor function
### Example
```lean
structure Point where
	x : Float
	y : Float

#check Point.mk
// Point.mk : Float -> Float -> Point

#check Point.mk 1.5 2.8
// {x := 1.5, y := 2.8} : Point
```
# Accessors
- All types have accessors with their name
```
Point.x
Point.y
```
# Struct-Specific Functions
```
def Point.modifyBoth (f : Float -> Float) (p : Point) : Point 
{x := f p.x, y := f p.y}
```