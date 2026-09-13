---
tags:
  - go
  - programming
---
```go
func myfunc(someparam string, someparam2 int) {
	// ...
	return "good"	
}
```
# Multiple Return Types
```go
func myfunc(a float64, b float64) (int, error) {
	// can return an error, you should do _, err = myfunc(...)
	if a == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}
```
# Struct/Class Method
```go
type Player struct {
	HP int,
	Level int
}

func (p *Player) hit(damage int) {
	p.HP -= damage;
}
```