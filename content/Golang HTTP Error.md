---
tags:
  - programming
  - go
  - web
---
```go
http.Error(w ResponseWriter, msg string, code int)
```
- Returns a response with status code a
- Returns the error message
- Ensures no further writes are done to the writer
# Example
```go
func createUser(w http.ResponseWriter, r *http.Request) {
	var user User
	err := json.NewDecoder(r.Body).Decode(&user)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
}
```