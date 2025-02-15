---
tags:
  - go
  - programming
  - web
---
```go
func enableCors(w *http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
	(*w).Header().Set("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
	(*w).Header().Set("Access-Control-Allow-Headers", "Accept, Content-Type, Content-Length, Authorization")
}

// then, for every route, set the header
func getRoot(w http.ResponseWriter, r *http.Request) {
	enableCors(&w)
	fmt.Printf("got / request\n")
	io.WriteString(w, "This is my website!\n")
}
```