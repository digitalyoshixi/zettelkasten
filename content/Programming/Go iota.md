---
tags:
  - programming
  - go
---
```go
type Direction int 
const (
	North Direction = iota // 0
	South Direction // 1
	East Direction // 2
	West Direction // 3
)
```
# iota Starting at 1
```go
type Direction int 
const (
	Unknown Direction = iota // 0
	North Direction // 1
	South Direction // 1
	East Direction // 2
	West Direction // 3
)
```