---
tags:
  - programming
  - haskell
---
# Example
![[Type Definition from Tree Representation-20260304225540793.webp]]
### Type
```haskell
data MathExpr = 
	  Leaf int
	| Unary (Int -> Int, MathExpr)
	| Binary (Int -> Int -> Int, MathExpr, MathExpr)
	
eval (Left v) = v
eval (Unary (f,t)) = f (eval t)
eval (Binary (f,l,r)) = f (eval l) (eval r)
```
### Implementing Tree
```haskell
t = Binary( (+),
			Binary((+)
				Unary(abs, 
					Unary ((0-),
						Leaf 3
					),
				Leaf 2
				),
			),
			Binary((*),
				Binary((+),
					Unary((0-),
						Leaf 1
					),
					Leaf 4
				),
				Leaf 7
			)
)
```