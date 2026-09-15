---
tags:
  - programming
  - go
  - web
---
```go
import (
	"net/http"
)

func homeHandler(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("html/home.html"))
	err := templ.Execute(w, nil);
	if err != nil {
		panic(err)
	}
}
```
# Nested Templates
```go
tmpl := template.Must(template.New("parent").Parse(parent))
tmpl = template.Must(tmpl.Parse(child))
tmpl.ExecuteTemplate(os.Stdout, "parent", data)
```