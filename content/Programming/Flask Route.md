---
tags:
  - web
  - programming
  - python
aliases:
  - URL Route
---
What should be triggered after the user sends data to a specific route on the website
```python
@app.route('/')
def index():
	return "<h1>MAIN PAGE<\h1>"
	
@app.route('/greet/<name>))
def greet(name):
	return f"HELLO {name}"
	
@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    return f"{int(num1) + int(num2)}"
```
The inputs are given as `string`, the return type must also be `string`
# [[Rest API|HTTP Request]]
```python
@app.route('/hello', methods = ['POST'])
def hello():
	if request.method == 'POST':
		console.log(request.form)
		return "wtf do u wanna do with POST man?"
	return "HELLO WORLD"
```
Run the designated [[Curl]] command to send the test requests.
![[Flask Route-20241004033027799.webp]]
The default request and the permitted one will always be GET
### [[HTTP Status Codes]]
```python
@app.route('/hello')
def hello():
	return "HELLO WORLD", 200
```
