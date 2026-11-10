---
tags:
  - programming
  - go
---
```go
decoder := json.NewDecoder(req.Body)
// anonymous struct
var t := struct {
	Name string
	Age int
}
err := decoder.Decode(&t)
if err != nil {
	panic(err)
}
log.Println(t.Name)
log.Println(t.Age)
```