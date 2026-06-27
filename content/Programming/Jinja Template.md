---
tags:
  - python
  - web
---
A [[Templating Language]] used in creating template [[Hypertext Markup Language|HTML]] files.
# Jinja Segments
In `app.py`
```python
@app.route('/')
def index():
    return render_template("index.html", myval="DAVID"
```
In `index.html`
```python
<body>
    HI {{myval}}
</body
```
The values will always typecasted as strings
Then
![[Jinja Template-20241004135526356.webp]]
# Jinja Blocks
Templates allow you to run python code within HTML.
`index.html`
```python
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
	<ul>
		{% for item in mylist%}
			{{ item }}
		{% endfor %}
	</ul>
</body>
</html>
```
