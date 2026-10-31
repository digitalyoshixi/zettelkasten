---
tags:
  - programming
  - go
  - web
aliases:
  - Golang NewServeMux()
---
An instance of a http request multiplexer with the [[Go HTTP Server]] library.
- By default, the `DefaultServeMux` is used (`http.ServeMux`)
- You can create a new multipleer with `NewServeMux()`
# Boilerplate Code
```go
mux := http.NewServeMux()
```