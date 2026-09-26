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
Example HTML:
```html
{{template "header"}}
Hello world! my name is {{.name}}
{{template "footer"}}
```

```html
{{define "header"}}
<header>
	<a href="/"> Home </a>
	<a href="/about"> About </a>
	<a href="/contact"> Contact </a>
</header>
{{end}}

{{define "footer"}}
<p>
Copyright 2026. All rights Reserved.
</p>
```
Example Go:

```go
tmpl, _ := template.ParseFiles("hello.html", "common.html")
templ.Execute(os.Stdout, map[string]string{
"name": "bokwon",
})
```